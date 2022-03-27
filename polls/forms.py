from django import forms
from .models import *

class PersonForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = ['group', 'name', 'duration', 'distance', 'image']
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'required': 'true'}))
    duration = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'required': 'true'}))
    distance = forms.DecimalField(required=True, widget=forms.NumberInput(attrs={'required': 'true'}))