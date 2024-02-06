# forms.py
from django import forms
from .models import *

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['gender']  

        widgets = {
            'gender': forms.RadioSelect(attrs={'class': 'gender-radio'}),
        }
class UserProfileForm1(forms.ModelForm):
    class Meta:
        model = Nurses
        fields = ['gender']  

        widgets = {
            'gender': forms.RadioSelect(attrs={'class': 'gender-radio'}),
        }

class YourModelForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['image']

class AppointmentModelForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields ="__all__"

