# Generated by Django 2.1.5 on 2019-05-12 07:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190512_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(error_messages={'blank': 'This is required', 'unique': 'This title is not unique'}, help_text='Unique Title', max_length=240, unique=True, verbose_name='Post Title'),
        ),
    ]
