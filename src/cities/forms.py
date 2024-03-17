from django import forms
from cities.models import City
from django.core.exceptions import ValidationError




class CityForm(forms.ModelForm):

    name = forms.CharField(label='Місто', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введіть назву міста'
    }))
    class Meta:
        model = City
        fields = ('name',)
    
    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if not name.replace(" ", "").isalpha():
    #         raise ValidationError("Введіть ільки літери")
    #     return name
        