# Generated by Django 2.0.2 on 2020-04-06 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_remove_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
    ]
