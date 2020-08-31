from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class OSatiForm(forms.ModelForm):
    class Meta:
        model = OdradjeniSati
        fields = ['pvremena']

class OSatiForm1(forms.ModelForm):
    class Meta:
        model = OdradjeniSati
        fields = ['kvremena']
   
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {
            'username': None,
            'email': None,
        }
        
class ZadaciForm(forms.ModelForm):
    class Meta:
        model = ListaZadataka
        fields = ['naziv', 'opis', 'status',]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nazivfirme', 'adresa', 'kontakt')

        
            
        
  