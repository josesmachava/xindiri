# Generated by Django 2.2.2 on 2020-09-21 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_auto_20200921_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='business',
            name='public_key',
            field=models.CharField(default='44f202d3a43501caab61cc3c064af052b407395684023707e200013ca658246b', editable=False, max_length=32),
        ),
        migrations.AlterField(
            model_name='productionapi',
            name='api_key',
            field=models.CharField(default='5cce19b3d6d900c581e34d4153f8719b', editable=False, max_length=32, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='sandboxapi',
            name='api_key',
            field=models.CharField(default='cefab0a0d1cec62e72cd9220d459550c', editable=False, max_length=32, primary_key=True, serialize=False, unique=True),
        ),
    ]