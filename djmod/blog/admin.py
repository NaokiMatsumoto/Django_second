from django.contrib import admin
from .models import PostModel
# Register your models here.


class PostModelAdmn(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'content',
        'publish',
        'publish_date',
        'active',
        'updated',
        'timestamp',
        'get_age'
    ]

    readonly_fields = ['updated', 'timestamp', 'get_age']

    def get_age(self, obj, *args, **kwargs):
        return str(obj.age)

    class Meta:
        model = PostModel


admin.site.register(PostModel, PostModelAdmn)
