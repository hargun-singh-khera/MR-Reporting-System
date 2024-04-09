from django.contrib import admin
from mr_reporting_app.models import *
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.forms import TextInput, Textarea
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import FilteredSelectMultiple
from .forms import *
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
    form = CityForm
    search_fields = ['state']
    # list_display = ('city', 'state', 'country')
    # autocomplete_fields = ['country', 'state']
    # list_filter = ('country', 'city', 'state')
    # search_fields = ['city']
    class Media:
        js = ('/static/js/dropdown_selection.js',)
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Add a CSS class to the country dropdown to identify it
        form.base_fields['country'].widget.attrs['class'] = 'country-dropdown'
        return form
    
    
class AreaMasterAdmin(admin.ModelAdmin):
    list_display = ('area', 'city')
    autocomplete_fields = ['city']
    search_fields = ['area']

# class DesignationMasterAdmin(admin.ModelAdmin):
#     list_display = ('designation',)


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
    list_display = ('name', 'username', 'email', 'mobile_number', 'area', 'designation', 'under', 'date_of_birth', 'date_of_joining', 'is_superuser')
    fieldsets = (
        ('User Creation Form', {'fields': ('email', 'username', 'name', 'mobile_number', 'area', 'designation', 'under', 'date_of_birth', 'date_of_joining', 'password', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    
    add_fieldsets = (
        ('User Creation Form', {
            'classes': ('wide',),
            'fields': ('email', 'username', 'name', 'password1', 'password2', 'is_active', 'is_staff')}
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
        designaion = form.cleaned_data.get('designation')
        subject = "Reset your account password"
        print("Email entered: ", email, "\nPassword:", password)
        message = f"""\
                    Hii, <strong>{name}</strong><br>
                    We just created your account. Please find your credentials below for accessing our MR Reporting System.<br>
                    Username: <strong>{username}</strong><br>
                    Password: <strong>{password}</strong><br>
                    Designation Alloted: <strong>{designaion}</strong><br>
                    We suggest you to change your password as soon as possible after you got logged in.
                    """
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, html_message=message)
    
class UnitMasterAdmin(admin.ModelAdmin):
    list_display = ('unit',)

class ProductMasterAdmin(admin.ModelAdmin):
    list_display = ('product', 'unit')

class DoctorMasterAdmin(admin.ModelAdmin):
    list_display = ('doctor_name', 'area','mobile_number')
    fieldsets = (
        (None, {'fields': ('doctor_name', 'area', 'mobile_number')}),
    )

class StockisterMasterAdmin(admin.ModelAdmin):
    list_display = ('stockist_name', 'address', 'area','mobile_number')
    fieldsets = (
        (None, {'fields': ('stockist_name', 'address', 'area','mobile_number')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('stockist_name', 'address', 'area','mobile_number')}
         ),
    )

class GiftMasterAdmin(admin.ModelAdmin):
    list_display = ('gift_name',)


class AreaMappingAdmin(admin.ModelAdmin):
    # pass
    title = ''
    form = CustomAreaMapping
    # list_display = ['user', ]
    

class RequestsMasterAdmin(admin.ModelAdmin):
    pass

class TourProgramAdmin(admin.ModelAdmin):
    form = TourProgramForm
    # pass

admin.site.register(CountryMaster, CountryMasterAdmin)
admin.site.register(StateMaster, StateMasterAdmin)
admin.site.register(CityMaster, CityMasterAdmin)
admin.site.register(AreaMaster, AreaMasterAdmin)
# admin.site.register(DesignationMaster, DesignationMasterAdmin)
admin.site.register(UserMaster, UserMasterAdmin)
admin.site.register(UnitMaster, UnitMasterAdmin)
admin.site.register(ProductMaster, ProductMasterAdmin)
admin.site.register(DoctorMaster, DoctorMasterAdmin)
admin.site.register(StockistMaster, StockisterMasterAdmin)
admin.site.register(GiftMaster, GiftMasterAdmin)
admin.site.register(UserAreaMapping, AreaMappingAdmin)
admin.site.register(RequestsMaster, RequestsMasterAdmin)
admin.site.register(TourProgram, TourProgramAdmin)