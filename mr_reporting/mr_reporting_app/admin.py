from django.contrib import admin
from mr_reporting_app.models import CountryMaster, StateMaster, CityMaster, AreaMaster, DesignationMaster, MRMaster, UnitMaster, ProductMaster, DoctorMaster, StockistMaster
# Register your models here.

class CountryMasterAdmin(admin.ModelAdmin):
    list_display = ('country',)

class StateMasterAdmin(admin.ModelAdmin):
    list_display = ('country', 'state')

class CityMasterAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'country')

class AreaMasterAdmin(admin.ModelAdmin):
    list_display = ('area', 'city')

class DesignationMasterAdmin(admin.ModelAdmin):
    list_display = ('designation',)

class MRMasterAdmin(admin.ModelAdmin):
    list_display = ('mr_name', 'area', 'designation', 'date_of_birth', 'date_of_joining','mobile_number')

class UnitMasterAdmin(admin.ModelAdmin):
    list_display = ('unit',)

class ProductMasterAdmin(admin.ModelAdmin):
    list_display = ('product', 'unit')

class DoctorMasterAdmin(admin.ModelAdmin):
    list_display = ('doctor_name', 'area','mobile_number')

class StockisterMasterAdmin(admin.ModelAdmin):
    list_display = ('stockist_name', 'address', 'area','mobile_number')

admin.site.register(CountryMaster, CountryMasterAdmin)
admin.site.register(StateMaster, StateMasterAdmin)
admin.site.register(CityMaster, CityMasterAdmin)
admin.site.register(AreaMaster, AreaMasterAdmin)
admin.site.register(DesignationMaster, DesignationMasterAdmin)
admin.site.register(MRMaster, MRMasterAdmin)
admin.site.register(UnitMaster, UnitMasterAdmin)
admin.site.register(ProductMaster, ProductMasterAdmin)
admin.site.register(DoctorMaster, DoctorMasterAdmin)
admin.site.register(StockistMaster, StockisterMasterAdmin)