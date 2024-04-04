# Generated by Django 5.0.2 on 2024-04-04 19:14

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DesignationMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GiftMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gift_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UnitMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CityMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.countrymaster')),
            ],
        ),
        migrations.CreateModel(
            name='AreaMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.citymaster')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.countrymaster')),
            ],
        ),
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=60, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('date_of_joining', models.DateField(null=True)),
                ('last_login', models.DateTimeField(default=datetime.datetime(2024, 4, 4, 19, 14, 48, 237357, tzinfo=datetime.timezone.utc), null=True)),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.areamaster')),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.designationmaster')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DoctorMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=10)),
                ('approval_status', models.BooleanField(default=False)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.areamaster')),
            ],
        ),
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.countrymaster')),
            ],
        ),
        migrations.AddField(
            model_name='citymaster',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.statemaster'),
        ),
        migrations.AddField(
            model_name='areamaster',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.statemaster'),
        ),
        migrations.CreateModel(
            name='StockistMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockist_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('mobile_number', models.CharField(max_length=10)),
                ('approval_status', models.BooleanField(default=False)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.areamaster')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.unitmaster')),
            ],
        ),
    ]