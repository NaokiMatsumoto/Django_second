# Generated by Django 2.1.5 on 2019-05-12 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190512_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='title',
            field=models.CharField(default='New Title', max_length=240),
            preserve_default=False,
        ),
    ]
