# Generated by Django 2.2.3 on 2019-07-17 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='transaction_id',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='transaction_status',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='transaction_status_code',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
