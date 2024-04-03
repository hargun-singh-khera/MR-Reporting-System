from django.contrib import admin
from mr_reporting_app.models import *
# Register your models here.

class CountryMasterAdmin(admin.ModelAdmin):
    list_display = ('country',)
    search_fields = ['country']

class StateMasterAdmin(admin.ModelAdmin):
    list_display = ('state', 'country')
    list_filter = ('state',)
    search_fields = ['state']
    autocomplete_fields = ['country']

class CityMasterAdmin(admin.ModelAdmin):
    search_fields = ['state']
    list_display = ('city', 'state', 'country')
    autocomplete_fields = ['country', 'state']
    list_filter = ('country', 'city', 'state')
    search_fields = ['city']
    
    
class AreaMasterAdmin(admin.ModelAdmin):
    list_display = ('area', 'city')
    autocomplete_fields = ['city']
    search_fields = ['area']

class DesignationMasterAdmin(admin.ModelAdmin):
    list_display = ('designation',)

class UserMasterAdmin(admin.ModelAdmin):
    pass
    # list_display = ('email', 'name', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login')
    # list_display = ('name', 'area', 'designation', 'date_of_birth', 'date_of_joining','mobile_number')

class UnitMasterAdmin(admin.ModelAdmin):
    list_display = ('unit',)

class ProductMasterAdmin(admin.ModelAdmin):
    list_display = ('product', 'unit')

class DoctorMasterAdmin(admin.ModelAdmin):
    list_display = ('doctor_name', 'area','mobile_number', 'approval_status')

class StockisterMasterAdmin(admin.ModelAdmin):
    list_display = ('stockist_name', 'address', 'area','mobile_number', 'approval_status')

class GiftMasterAdmin(admin.ModelAdmin):
    list_display = ('gift_name',)

admin.site.register(CountryMaster, CountryMasterAdmin)
admin.site.register(StateMaster, StateMasterAdmin)
admin.site.register(CityMaster, CityMasterAdmin)
admin.site.register(AreaMaster, AreaMasterAdmin)
admin.site.register(DesignationMaster, DesignationMasterAdmin)
admin.site.register(UserMaster, UserMasterAdmin)
admin.site.register(UnitMaster, UnitMasterAdmin)
admin.site.register(ProductMaster, ProductMasterAdmin)
admin.site.register(DoctorMaster, DoctorMasterAdmin)
admin.site.register(StockistMaster, StockisterMasterAdmin)
admin.site.register(GiftMaster, GiftMasterAdmin)