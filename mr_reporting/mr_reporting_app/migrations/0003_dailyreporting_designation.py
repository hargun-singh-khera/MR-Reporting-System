# Generated by Django 5.0.4 on 2024-04-22 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('mr_reporting_app', '0002_remove_dailyreporting_designation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyreporting',
            name='designation',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
            preserve_default=False,
        ),
    ]