# Generated by Django 2.2.2 on 2020-11-16 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20201110_2313'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Business',
            new_name='Startup',
        ),
        migrations.AlterField(
            model_name='api',
            name='live_api',
            field=models.CharField(default='77f6670a19de93d30f209049511800da', editable=False, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='test_api',
            field=models.CharField(default='d46bb74d50296d4af267e5727f17d715', editable=False, max_length=32, unique=True),
        ),
    ]
