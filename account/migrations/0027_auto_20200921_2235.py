# Generated by Django 2.2.2 on 2020-09-21 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_auto_20200921_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='public_key',
            field=models.CharField(default='eae636cb9236908b901b4bedb0f8cf92fe9507b843f549d6580c26a60ba0c352', editable=False, max_length=32),
        ),
        migrations.AlterField(
            model_name='productionapi',
            name='api_key',
            field=models.CharField(default='c6f7e3a76fad4fae7aa5506ebed83ee5', editable=False, max_length=32, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='sandboxapi',
            name='api_key',
            field=models.CharField(default='206a49873cb418584f86fd60231c99a3', editable=False, max_length=32, primary_key=True, serialize=False, unique=True),
        ),
    ]
