from django import forms
from .models import *
from django.contrib.admin.widgets import FilteredSelectMultiple

class CustomAreaMapping(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=UserMaster.objects.filter(is_superuser=False)
    )
    areas = forms.ModelMultipleChoiceField(
        queryset=CityMaster.objects.all(),
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



class TourProgramForm(forms.ModelForm):
    pass
    employee = forms.ModelChoiceField(
        queryset=UserMaster.objects.filter(is_superuser=False),
        # queryset=UserMaster.objects.all(),
        # widget=forms.MultipleChoiceField(attrs={'style': 'width: 200px;'})
    )
    # from_area = forms.ModelChoiceField(
    #     # queryset=UserAreaMapping.objects.none(),
    #     queryset=AreaMaster.objects.all(),
    #     required=True,
    #     # widget=forms.Select(attrs={'style': 'width: 200px;'})
        
    # )
    # to_area = forms.ModelChoiceField(
    #     queryset=AreaMaster.objects.all(),
    #     required=True,
    #     # widget=forms.Select(attrs={'style': 'width: 200px;'})
    # )

class CityForm(forms.ModelForm):
    country = forms.ModelChoiceField(
        queryset=CountryMaster.objects.all(),
        widget=forms.Select(attrs={'style': 'width: 200px;'}),
        required=True
    )
    state = forms.ModelChoiceField(
        queryset=StateMaster.objects.all(),
        widget=forms.Select(attrs={'style': 'width: 200px;'}),
        required=True
    )
    city = forms.CharField(max_length=100, required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'country' in self.initial:
            country_id = self.initial['country']
            self.fields['state'].queryset = StateMaster.objects.filter(country_id=country_id)