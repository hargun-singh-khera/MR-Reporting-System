from django.contrib import admin
from mr_reporting_app.models import *
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.forms import TextInput, Textarea
from django.core.mail import send_mail
from django.conf import settings
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
    list_filter = ('email', 'name', 'name', 'is_active', 'is_staff', 'is_superuser')
    list_display = ('name', 'username', 'email', 'mobile_number', 'is_active', 'is_staff', 'is_superuser')
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
    def save_model(self, request, obj, form, change):
        email = form.cleaned_data.get('email')
        if UserMaster.objects.filter(email=email).exists():
            raise("Email already exists")
        if "_addanother" in request.POST:
            self.send_email_to_user(request, form, email)
            # pass
        elif "_save" in request.POST:
            self.send_email_to_user(request, form, email)
            # pass
        super().save_model(request, obj, form, change)
        
    
        
    def send_email_to_user(self, request, form, email):
        print("Email sent")
        name = form.cleaned_data.get('name')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        subject = "Reset your account password"
        print("Email entered: ", email, "\nassword:", password)
        message = f"Hii , {name} \nWe just created your account. Please find your credentials below.\nUsername:{username}\nPassword:{password}\nWe suggest you to change your password as soon as possible after you got logged in."
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)
    

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

def send_email_to_user(email):
        subject = "This email is from Django server"
        message = "This is our test message from Django server email"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

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