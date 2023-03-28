from django import forms
from cities.models import City
from trains.models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Номер потягу', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введіть номер потягу'
    }))
    travel_time = forms.IntegerField(label='Час в дорозі', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введіть час в дорозі'
    }))
    from_city = forms.ModelChoiceField(label='Звідки', queryset=City.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}
    ))
    to_city = forms.ModelChoiceField(label='Куди', queryset=City.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}
    ))

    class Meta:
        model = Train
        fields = '__all__'