from django.db import models

# Create your models here.
class CountryMaster(models.Model):
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.country

class StateMaster(models.Model):
    state = models.CharField(max_length=100)
    country = models.ForeignKey(CountryMaster, on_delete = models.CASCADE)
    def __str__(self):
        return self.state

class CityMaster(models.Model):
    city = models.CharField(max_length=100)
    state = models.ForeignKey(StateMaster, on_delete = models.CASCADE)
    country = models.ForeignKey(CountryMaster, on_delete = models.CASCADE)
    def __str__(self):
        return self.city

class AreaMaster(models.Model):
    area = models.CharField(max_length=100)
    city = models.ForeignKey(CityMaster, on_delete = models.CASCADE)
    def __str__(self):
        return self.area

class DesignationMaster(models.Model):
    designation = models.CharField(max_length=100)
    def __str__(self):
        return self.designation

class MRMaster(models.Model):
    mr_name = models.CharField(max_length=100)
    area = models.ForeignKey(AreaMaster, on_delete = models.CASCADE)
    designation = models.ForeignKey(DesignationMaster, on_delete = models.CASCADE)
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    mobile_number = models.CharField(max_length=10)

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
    def __str__(self):
        return self.doctor_name

class StockistMaster(models.Model):
    stockist_name = models.CharField(max_length=100)
    address = models.TextField()
    area = models.ForeignKey(AreaMaster, on_delete = models.CASCADE)
    mobile_number = models.CharField(max_length=10)
    def __str__(self):
        return self.stockist_name
