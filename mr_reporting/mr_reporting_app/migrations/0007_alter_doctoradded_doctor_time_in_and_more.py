# Generated by Django 5.0.4 on 2024-04-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mr_reporting_app', '0006_alter_doctoradded_doctor_time_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctoradded',
            name='doctor_time_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='doctoradded',
            name='doctor_time_out',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='stockistadded',
            name='stockist_time_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='stockistadded',
            name='stockist_time_out',
            field=models.DateField(),
        ),
    ]
