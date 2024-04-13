# Generated by Django 5.0.4 on 2024-04-13 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mr_reporting_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailyreporting',
            old_name='destination_area_id',
            new_name='destination_area',
        ),
        migrations.RenameField(
            model_name='dailyreporting',
            old_name='doctor_id',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='dailyreporting',
            old_name='employee_id',
            new_name='employee',
        ),
        migrations.RenameField(
            model_name='dailyreporting',
            old_name='gift_id',
            new_name='gift',
        ),
        migrations.RenameField(
            model_name='dailyreporting',
            old_name='gift_unit_id',
            new_name='gift_unit',
        ),
        migrations.RenameField(
            model_name='dailyreporting',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='dailyreporting',
            old_name='product_unit_id',
            new_name='product_unit',
        ),
        migrations.RenameField(
            model_name='dailyreporting',
            old_name='source_area_id',
            new_name='source_area',
        ),
        migrations.RenameField(
            model_name='dailyreporting',
            old_name='stockist_id',
            new_name='stockist',
        ),
    ]
