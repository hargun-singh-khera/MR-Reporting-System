# Generated by Django 5.0.4 on 2024-04-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mr_reporting_app', '0005_tourprogram_blocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctoradded',
            name='doctor_time_in',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='doctoradded',
            name='doctor_time_out',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='giftadded',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productadded',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stockistadded',
            name='stockist_time_in',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='stockistadded',
            name='stockist_time_out',
            field=models.DateTimeField(),
        ),
    ]
