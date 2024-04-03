from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
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

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You must provide a valid email")
    
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class UserMaster(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, blank=True, default='')
    email = models.EmailField(blank=True, default='', unique=True)
    
    area = models.ForeignKey(AreaMaster, on_delete = models.CASCADE, null=True)
    designation = models.ForeignKey(DesignationMaster, on_delete = models.CASCADE, null=True)
    date_of_birth = models.DateField(blank=False, null=True)
    date_of_joining = models.DateField(blank=False, null=True)
    mobile_number = models.CharField(max_length=10)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    # EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    # class Meta:
    #     verbose_name = 'UserMaster'
    #     verbose_name_plural = 'UserMasters'

    # def get_full_name(self):
    #     return self.name
    
    # def get_short_name(self):
    #     return self.name or self.email.split('@')[0]
    
