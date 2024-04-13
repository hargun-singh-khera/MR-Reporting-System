# Generated by Django 5.0.4 on 2024-04-13 15:26

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CityMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CountryMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GiftMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gift_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=20, unique=True)),
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
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('under', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.areamaster')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='areamaster',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.citymaster'),
        ),
        migrations.AddField(
            model_name='citymaster',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.countrymaster'),
        ),
        migrations.AddField(
            model_name='areamaster',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.countrymaster'),
        ),
        migrations.CreateModel(
            name='DoctorMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.areamaster')),
            ],
        ),
        migrations.CreateModel(
            name='RequestsMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_status', models.BooleanField(default=False)),
                ('request_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100, unique=True)),
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
                ('stockist_name', models.CharField(max_length=100, unique=True)),
                ('address', models.TextField()),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.areamaster')),
            ],
        ),
        migrations.CreateModel(
            name='TourProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_tour', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_tourprograms', to=settings.AUTH_USER_MODEL)),
                ('from_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_area', to='mr_reporting_app.areamaster')),
                ('to_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_area', to='mr_reporting_app.areamaster')),
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
        migrations.CreateModel(
            name='DailyReporting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('date_of_working', models.CharField(max_length=20)),
                ('doctor_time_in', models.CharField(max_length=10)),
                ('doctor_time_out', models.CharField(max_length=10)),
                ('product_quantity', models.CharField(max_length=10)),
                ('gift_quantity', models.CharField(max_length=10)),
                ('stockist_time_in', models.CharField(max_length=10)),
                ('stockist_time_out', models.CharField(max_length=10)),
                ('destination_area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_area', to='mr_reporting_app.areamaster')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('source_area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_area', to='mr_reporting_app.areamaster')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.doctormaster')),
                ('gift_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.giftmaster')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.productmaster')),
                ('stockist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr_reporting_app.stockistmaster')),
                ('gift_unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_unit_id', to='mr_reporting_app.unitmaster')),
                ('product_unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_unit_id', to='mr_reporting_app.unitmaster')),
            ],
        ),
        migrations.CreateModel(
            name='UserAreaMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areas', models.ManyToManyField(to='mr_reporting_app.areamaster')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
