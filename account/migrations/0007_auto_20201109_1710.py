# Generated by Django 2.2.2 on 2020-11-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20201109_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='live_api',
            field=models.CharField(default='6f49e7337aee5e0ed12e454d4bb18296', editable=False, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='test_api',
            field=models.CharField(default='cecdb04d885be3a90409581a6d99c6c8', editable=False, max_length=32, unique=True),
        ),
    ]