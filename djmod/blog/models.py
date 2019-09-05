from datetime import timedelta, datetime, date
from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone

from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.utils.timesince import timesince
from django.dispatch import receiver


def validation_error_email(value):
    if '0' in value:
        return value
    else:
        raise ValidationError('Not a good email')

def validation_justin(value):
    if 'justin' in value:
        return value
    else:
        raise ValidationError('Not a good email')


PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
)


class PostModelQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)

    def post_title_item(self, value):
        return self.filter(title__icontains=value)


class PostModelManger(models.Manager):

    def get_queryset(self):
        return PostModelQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        qs = super(PostModelManger, self).all(*args, **kwargs).active()
        qs = self.get_queryset().active()
        return qs


    def get_timeframe(self, date1, date2):
        qs = self.get_queryset()
        qs_time_1 = qs.filter(publish_date__gte=date1)
        qs_time_2 = qs.filter(publish_date__lt=date2)
        final_qs = (qs_time_1 | qs_time_2).distinct()
        return final_qs

class TestModes(models.Model):
    id = models.AutoField(primary_key=True)


class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField(blank=True)
    title = models.CharField(
        max_length=240, verbose_name='Post Title', unique=True, error_messages={
            'unique': 'This title is not unique',
            'blank': 'This is required'
        },
        help_text='Unique Title'
    )
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=128, choices=PUBLISH_CHOICES, default='draft')
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.EmailField(max_length=240, validators=[validation_error_email, validation_justin], null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = PostModelManger()
    other = PostModelManger()
    # save = PostModelManger()

    def save(self, *args, **kwargs):
        # if not self.slug and self.title:
        #     self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        # unique_together = [{}]

    def __str__(self):
        return smart_text(self.title)

    @property
    def age(self):
        if self.publish == 'publish':
            now = timezone.now()
            publish_time = datetime.combine(
                self.publish_date,
                datetime.now().min.time()
            )
            try:
                difference = now - publish_time
            except:
                return 'Unknown'
            if difference <= timedelta(minutes=1):
                return "just now"

            return timesince(self.publish_date)
        return "Not published"


@receiver(pre_save, sender=PostModel)
def blog_post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    print(instance.title)
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)


@receiver(post_save, sender=PostModel)
def blog_post_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    print('After save')
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()


