# Generated by Django 2.2.2 on 2020-11-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20201117_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='live_api',
            field=models.CharField(default='e00218e22d79106569945da81dca6ba5', editable=False, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='test_api',
            field=models.CharField(default='bc8213b1dffb907df3f65317131d8b0e', editable=False, max_length=32, unique=True),
        ),
    ]
