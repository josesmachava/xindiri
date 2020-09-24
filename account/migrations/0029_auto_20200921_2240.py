# Generated by Django 2.2.2 on 2020-09-21 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0028_auto_20200921_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='public_key',
            field=models.CharField(default='4a1c6942f297aceb1a73211c75e6a8f8b00e74088720b08a1aaba49ee3e773a0', editable=False, max_length=32),
        ),
        migrations.AlterField(
            model_name='productionapi',
            name='api_key',
            field=models.CharField(default='32dfbb2dc9c513dc3c2fb41a3705efa1', editable=False, max_length=32, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='sandboxapi',
            name='api_key',
            field=models.CharField(default='8b84805c912f35048cea0f67005bcd29', editable=False, max_length=32, primary_key=True, serialize=False, unique=True),
        ),
    ]
