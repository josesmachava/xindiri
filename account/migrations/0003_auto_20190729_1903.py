# Generated by Django 2.2.3 on 2019-07-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190729_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_instructor',
            new_name='is_business',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=1, max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]