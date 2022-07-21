from django import forms
from cities.models import City


class HtmlForm(forms.Form):
    name = forms.CharField(label='Город')


class CityForm(forms.ModelForm):
    """Редактируем отображение формы через классы bootstrap widget!!!"""
    name = forms.CharField(label='Город', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название города'
    }))
    class Meta:
        model = City
        fields = ('name',)