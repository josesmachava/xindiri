# Generated by Django 2.2.2 on 2020-11-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201109_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='live_api',
            field=models.CharField(default='b543fc2084a9a31a07dfa7d70d795c00', editable=False, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='test_api',
            field=models.CharField(default='d70d1cae2469edd959604cfdf5321ec8', editable=False, max_length=32, unique=True),
        ),
    ]
