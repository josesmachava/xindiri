# Generated by Django 2.2.2 on 2020-10-17 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordpress', '0002_transaction_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='first_name',
        ),
    ]