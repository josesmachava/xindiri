# Generated by Django 2.2.2 on 2020-09-29 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0005_auto_20200629_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255)),
                ('amount', models.CharField(max_length=255)),
                ('mpesaReturn', models.TextField()),
                ('reference', models.CharField(max_length=255)),
                ('api_key', models.CharField(max_length=255)),
                ('public_key', models.TextField()),
                ('transaction_id', models.CharField(max_length=255)),
                ('transaction_status_code', models.CharField(max_length=255)),
                ('transaction_status', models.CharField(max_length=255)),
                ('website', models.URLField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
