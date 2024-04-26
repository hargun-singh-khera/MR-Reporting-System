from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission


# Create your models here.
class CountryMaster(models.Model):
    country = models.CharField(max_length=100, blank=True, null=True, unique=True)
    def __str__(self):
        return self.country

class StateMaster(models.Model):
    country = models.ForeignKey(CountryMaster, on_delete=models.CASCADE, null=False)
    state = models.CharField(max_length=100, blank=False, null=False, unique=True)
    def __str__(self):
        return self.state

class CityMaster(models.Model):
    country = models.ForeignKey(CountryMaster, on_delete=models.CASCADE, null=False)
    state = models.ForeignKey(StateMaster, on_delete=models.CASCADE, null=False)
    city = models.CharField(max_length=100, blank=False, null=False, unique=True)
    def __str__(self):
        return self.city
    
class AreaMaster(models.Model):
    country = models.ForeignKey(CountryMaster, on_delete=models.CASCADE, null=False)
    state = models.ForeignKey(StateMaster, on_delete=models.CASCADE, null=False)
    city = models.ForeignKey(CityMaster, on_delete=models.CASCADE, null=False)
    area = models.CharField(max_length=100, blank=False, null=False, unique=True)
    def __str__(self):
        return self.area

# class DesignationMaster(models.Model):
#     designation = models.CharField(max_length=100)
#     def __str__(self):
#         return self.designation

class UnitMaster(models.Model):
    unit = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.unit

class ProductMaster(models.Model):
    product = models.CharField(max_length=100)
    unit = models.ForeignKey(UnitMaster, on_delete = models.CASCADE)
    def __str__(self):
        return self.product
   
class DoctorMaster(models.Model):
    doctor_name = models.CharField(max_length=100)
    country = models.ForeignKey(CountryMaster, on_delete=models.CASCADE, null=False, blank=False)
    state = models.ForeignKey(StateMaster, on_delete=models.CASCADE, null=False)
    city = models.ForeignKey(CityMaster, on_delete=models.CASCADE, null=False)
    area = models.ForeignKey(AreaMaster, on_delete = models.CASCADE)
    mobile_number = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.doctor_name

class GiftMaster(models.Model):
    gift_name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.gift_name

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError("You must provide an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        # self.send_email_to_user(email)
        return user

    def create_superuser(self, email, username, password, **other_fields):
        # Exclude ForeignKey fields for superuser creation
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        # other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        return self.create_user(email, username, password, **other_fields)

class UserMaster(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, blank=False)
    username = models.CharField(max_length=60, unique=False)
    email = models.EmailField(unique=True)

    area = models.ForeignKey(AreaMaster, on_delete = models.CASCADE, null=True, blank=False)
    designation = models.ForeignKey(Group, on_delete = models.CASCADE, null=True)
    date_of_birth = models.DateField(blank=False, null=True)
    date_of_joining = models.DateField(blank=False, null=True)
    last_login = models.DateTimeField(default=timezone.now)
    mobile_number = models.CharField(max_length=10, unique=True)
    under = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    def __str__(self):
        return self.name
    
    
@receiver(post_save, sender=UserMaster)
def grant_user_permissions(sender, instance, created, **kwargs):
    if created:  # Only run this logic when a new user is created
        user_group = instance.designation  # Retrieve the group associated with the user
        if user_group:
            permissions = Permission.objects.filter(group=user_group)  # Retrieve permissions associated with that group
            instance.user_permissions.set(permissions)  # Assign permissions to the user


class StockistMaster(models.Model):
    stockist_name = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    country = models.ForeignKey(CountryMaster, on_delete=models.CASCADE, null=False, blank=False)
    state = models.ForeignKey(StateMaster, on_delete=models.CASCADE, null=False)
    city = models.ForeignKey(CityMaster, on_delete=models.CASCADE, null=False)
    area = models.ForeignKey(AreaMaster, on_delete = models.CASCADE)
    mobile_number = models.CharField(max_length=10, unique=True)
    

    def __str__(self):
        return self.stockist_name


class UserAreaMapping(models.Model):
    # pass
    user = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    areas = models.ManyToManyField(AreaMaster)

    def __str__(self):
        return str(self.user)
    
    
class TourProgram(models.Model):
    employee = models.ForeignKey(UserMaster, on_delete=models.CASCADE, blank=False, related_name='employee_tourprograms')
    date_of_tour = models.DateField(null=False, blank=False)
    from_area = models.ForeignKey(AreaMaster, on_delete=models.CASCADE, blank=False, related_name='from_area')
    to_area = models.ForeignKey(AreaMaster, on_delete=models.CASCADE, blank=False, related_name='to_area')
    submitted = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)


class DailyReporting(models.Model):
    employee = models.ForeignKey(UserMaster, on_delete=models.CASCADE, related_name='employee_id')
    designation = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_of_working = models.CharField(max_length=20)
    source_area = models.ForeignKey(AreaMaster, on_delete=models.CASCADE, related_name='source_area')
    destination_area = models.ForeignKey(AreaMaster, on_delete=models.CASCADE, related_name='destination_area')


class DoctorAdded(models.Model):
    daily_reporting = models.ForeignKey(DailyReporting, on_delete=models.CASCADE, related_name='daily_reporting')
    doctor = models.ForeignKey(DoctorMaster, on_delete = models.CASCADE)
    doctor_time_in = models.TimeField()
    doctor_time_out = models.TimeField()
    status = models.BooleanField(default=False)


class ProductAdded(models.Model):
    product = models.ForeignKey(ProductMaster, on_delete=models.CASCADE)
    unit = models.ForeignKey(UnitMaster, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    doctor = models.ForeignKey(DoctorMaster, on_delete=models.CASCADE)
    daily_reporting = models.ForeignKey(DailyReporting, on_delete=models.CASCADE)

class GiftAdded(models.Model):
    gift = models.ForeignKey(GiftMaster, on_delete=models.CASCADE)
    unit = models.ForeignKey(UnitMaster, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    doctor = models.ForeignKey(DoctorMaster, on_delete=models.CASCADE)
    daily_reporting = models.ForeignKey(DailyReporting, on_delete=models.CASCADE)

class StockistAdded(models.Model):
    stockist = models.ForeignKey(StockistMaster, on_delete=models.CASCADE)
    stockist_time_in = models.TimeField()
    stockist_time_out = models.TimeField()
    daily_reporting = models.ForeignKey(DailyReporting, on_delete=models.CASCADE)


