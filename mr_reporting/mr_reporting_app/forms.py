from django import forms
from .models import *
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class CustomAreaMapping(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=UserMaster.objects.filter(is_superuser=False)
    )
    areas = forms.ModelMultipleChoiceField(
        queryset=AreaMaster.objects.all(),
        required=True,
        widget=FilteredSelectMultiple(
            verbose_name='Areas',
            is_stacked=False,
        )
    )

    class Meta:
        model = UserAreaMapping
        verbose_name = "Area Mapping"
        fields = ['user', 'areas']

    def __init__(self, *args, **kwargs):
        super(CustomAreaMapping, self).__init__(*args, **kwargs)
        self.fields['areas'].label = 'Areas'


    def save(self, commit=True):
        print("Save method called!")
        instance = super().save(commit=False) 
        print(f"Instance data before save: {instance}")
        print(f"Selected areas: {self.cleaned_data['areas']}")
        instance.save()  
        selected_area = self.cleaned_data['areas'].first()
        instance.areas.add(selected_area)
        return instance


class CityForm(forms.ModelForm):
    country = forms.ModelChoiceField(
        queryset=CountryMaster.objects.all(),
        widget=forms.Select(attrs={'id': 'id_country'}),
    )
    state = forms.ModelChoiceField(
        queryset=StateMaster.objects.none(),
        widget=forms.Select(attrs={'id': 'id_state'}),
    )
    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        country_id = kwargs.get('initial', {}).get('country', None)  
        if country_id:
            try:
                print("inside of country_id " + country_id)
                # Assuming CountryMaster has a field with unique values like name
                country = CountryMaster.objects.get(id=country_id)  # Adjust field name
                self.fields['state'].queryset = StateMaster.objects.filter(country=country)
            except CountryMaster.DoesNotExist:
                pass  # Handle case where country doesn't exist
        else:
            self.fields['country'].queryset = CountryMaster.objects.all()
            self.fields['state'].queryset = StateMaster.objects.all() # Reset city queryset


class AreaForm(forms.ModelForm):
    country = forms.ModelChoiceField(
        queryset=CountryMaster.objects.all(),
        widget=forms.Select(attrs={'id': 'id_country'}),
    )
    state = forms.ModelChoiceField(
        queryset=StateMaster.objects.none(),
        widget=forms.Select(attrs={'id': 'id_state'}),
    )
    city = forms.ModelChoiceField(
        queryset=CityMaster.objects.none(),
        widget=forms.Select(attrs={'id': 'id_city'}),
    )
    area = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(AreaForm, self).__init__(*args, **kwargs)
        country_id = kwargs.get('initial', {}).get('country', None)
        state_id = kwargs.get('initial', {}).get('state', None)
        if country_id:
            try:
                print("inside of country_id " + country_id)
                # Assuming CountryMaster has a field with unique values like name
                country = CountryMaster.objects.get(id=country_id)  # Adjust field name
                self.fields['state'].queryset = StateMaster.objects.filter(country=country)
                if state_id:
                    try:
                        print("inside of state_id " + state_id)
                        # Assuming CountryMaster has a field with unique values like name
                        state = StateMaster.objects.get(id=state_id)  # Adjust field name
                        self.fields['city'].queryset = CityMaster.objects.filter(state=state)
                    except CountryMaster.DoesNotExist:
                        pass  # Handle case where country doesn't exist  
            except CountryMaster.DoesNotExist:
                pass  # Handle case where country doesn't exist
        else:
            self.fields['country'].queryset = CountryMaster.objects.all()
            self.fields['state'].queryset = StateMaster.objects.all()
            self.fields['city'].queryset = CityMaster.objects.all()  # Reset city queryset


class CustomUserCreationForm(UserCreationForm):
    # country = forms.ModelChoiceField(
    #     queryset=CountryMaster.objects.all(),
    #     widget=forms.Select(attrs={'id': 'id_country'}),
    # )
    # state = forms.ModelChoiceField(
    #     queryset=StateMaster.objects.none(),
    #     widget=forms.Select(attrs={'id': 'id_state'}),
    # )
    # city = forms.ModelChoiceField(
    #     queryset=CityMaster.objects.none(),
    #     widget=forms.Select(attrs={'id': 'id_city'}),
    # )
    
    class Meta:
        model = UserMaster
        fields = '__all__'

    def clean_username(self):
        # Override the clean_username method to remove uniqueness validation
        return self.cleaned_data["username"]
    
    def clean(self):
        cleaned_data = super().clean()
        dob = cleaned_data.get('date_of_birth')
        doj = cleaned_data.get('date_of_joining')

        # Check if DOB and DOJ are the same
        if dob and doj and dob == doj:
            raise ValidationError("Date of birth and date of joining cannot be the same.")

        # Check if DOB year is greater than DOJ year
        if dob and doj and dob.year >= doj.year:
            raise ValidationError("Date of birth year should be less than date of joining year.")
        
        return cleaned_data

class TourProgramForm(forms.ModelForm):
    employee = forms.ModelChoiceField(
        queryset=UserMaster.objects.filter(is_superuser=False),
        widget=forms.Select(attrs={'id': 'id_employee'}),
    )
    from_area = forms.ModelChoiceField(
        queryset=AreaMaster.objects.none()
    )
    to_area = forms.ModelChoiceField(
        queryset=AreaMaster.objects.none()
    )
    def __init__(self, *args, **kwargs):
        super(TourProgramForm, self).__init__(*args, **kwargs)
        employee_id = kwargs.get('initial', {}).get('employee', None)  
        if employee_id:
            try:
                print("inside of employee_id " + employee_id)
                # Assuming CountryMaster has a field with unique values like name
                user_instance = UserMaster.objects.get(id=employee_id)  # Adjust field name
                user_id = user_instance.id
                user_instance_mapping = UserAreaMapping.objects.get(user_id=user_id)
                areas_related = user_instance_mapping.areas.all()
                self.fields['from_area'].queryset = areas_related
                self.fields['to_area'].queryset = areas_related
            except CountryMaster.DoesNotExist:
                pass  # Handle case where country doesn't exist
        else:
            pass
            self.fields['employee'].queryset = UserMaster.objects.filter(is_superuser=False)
            self.fields['from_area'].queryset = AreaMaster.objects.all() 
            self.fields['to_area'].queryset = AreaMaster.objects.all()# Reset city queryset