from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CountryMaster(models.Model):
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.country

class StateMaster(models.Model):
    country = models.ForeignKey(CountryMaster, on_delete = models.CASCADE)
    state = models.CharField(max_length=100)
    def __str__(self):
        return self.state

class CityMaster(models.Model):
    country = models.ForeignKey(CountryMaster, on_delete = models.CASCADE)
    state = models.ForeignKey(StateMaster, on_delete = models.CASCADE)
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.city

class AreaMaster(models.Model):
    country = models.ForeignKey(CountryMaster, on_delete = models.CASCADE)
    state = models.ForeignKey(StateMaster, on_delete = models.CASCADE)
    city = models.ForeignKey(CityMaster, on_delete = models.CASCADE)
    area = models.CharField(max_length=100)
    def __str__(self):
        return self.area

class DesignationMaster(models.Model):
    designation = models.CharField(max_length=100)
    def __str__(self):
        return self.designation

# class EmployeeMaster(models.Model):
    # name = models.CharField(max_length=100)
    # area = models.ForeignKey(AreaMaster, on_delete = models.CASCADE)
    # designation = models.ForeignKey(DesignationMaster, on_delete = models.CASCADE)
    # date_of_birth = models.DateField()
    # date_of_joining = models.DateField()
    # mobile_number = models.CharField(max_length=10)

class UnitMaster(models.Model):
    unit = models.CharField(max_length=20)
    def __str__(self):
        return self.unit

class ProductMaster(models.Model):
    product = models.CharField(max_length=100)
    unit = models.ForeignKey(UnitMaster, on_delete = models.CASCADE)
    def __str__(self):
        return self.product
   
class DoctorMaster(models.Model):
    doctor_name = models.CharField(max_length=100)
    area = models.ForeignKey(AreaMaster, on_delete = models.CASCADE)
    mobile_number = models.CharField(max_length=10)
    approval_status = models.BooleanField(default=False)
    def __str__(self):
        return self.doctor_name

class StockistMaster(models.Model):
    stockist_name = models.CharField(max_length=100)
    address = models.TextField()
    area = models.ForeignKey(AreaMaster, on_delete = models.CASCADE)
    mobile_number = models.CharField(max_length=10)
    approval_status = models.BooleanField(default=False)
    def __str__(self):
        return self.stockist_name

class GiftMaster(models.Model):
    gift_name = models.CharField(max_length=100)

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
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(unique=True)

    area = models.ForeignKey(AreaMaster, on_delete = models.CASCADE, null=True)
    designation = models.ForeignKey(DesignationMaster, on_delete = models.CASCADE, null=True)
    date_of_birth = models.DateField(blank=False, null=True)
    date_of_joining = models.DateField(blank=False, null=True)
    last_login = models.DateTimeField(default=timezone.now)
    mobile_number = models.CharField(max_length=10, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username