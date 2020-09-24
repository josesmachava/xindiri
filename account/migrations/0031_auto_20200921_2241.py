# Generated by Django 2.2.2 on 2020-09-21 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0030_auto_20200921_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='nuqit',
            new_name='nuit',
        ),
        migrations.AlterField(
            model_name='business',
            name='public_key',
            field=models.CharField(default='f2afef8e625c51a2ab3a6344c0079a7325f766779f257907a8845ac9cf41d08b', editable=False, max_length=32),
        ),
        migrations.AlterField(
            model_name='productionapi',
            name='api_key',
            field=models.CharField(default='dd9c631a1f86c11fa15a37e48646022c', editable=False, max_length=32, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='sandboxapi',
            name='api_key',
            field=models.CharField(default='f3648452070715b9f5a6ccacee5cb5b1', editable=False, max_length=32, primary_key=True, serialize=False, unique=True),
        ),
    ]
