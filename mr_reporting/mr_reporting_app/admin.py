from django.contrib import admin
from mr_reporting_app.models import *
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.forms import TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
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


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserMaster
        fields = '__all__'

class UserMasterAdmin(admin.ModelAdmin):
    form = CustomUserCreationForm
    model = UserMaster
    ordering = ('name',)
    search_fields = ('email', 'username', 'name',)
    list_filter = ('email', 'name', 'name', 'is_active', 'is_staff')
    list_display = ('name', 'username', 'email', 'mobile_number', 'is_active', 'is_staff')
    fieldsets = (
        ('User Creation Form', {'fields': ('email', 'username', 'name', 'mobile_number', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    
    add_fieldsets = (
        ('User Creation Form', {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )
    

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