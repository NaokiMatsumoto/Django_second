# Generated by Django 2.1.5 on 2019-05-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20190513_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='slug2',
            field=models.SlugField(null=True),
        ),
    ]