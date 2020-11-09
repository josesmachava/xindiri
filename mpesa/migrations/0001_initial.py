# Generated by Django 2.2.2 on 2020-11-09 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('mpesaReturn', models.TextField()),
                ('reference', models.CharField(max_length=255)),
                ('api_key', models.CharField(max_length=255)),
                ('public_key', models.TextField()),
                ('transaction_id', models.CharField(max_length=255)),
                ('transaction_status_code', models.CharField(max_length=255)),
                ('transaction_status', models.CharField(max_length=255)),
                ('website', models.URLField()),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
