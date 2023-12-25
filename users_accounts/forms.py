from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserProfile, WithdrawalRequest
from django import forms

class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class LoginUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('__all__')

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255)

class AcceptTOSForm(forms.Form):
    accepted = forms.BooleanField(label='I accept the Terms of Service')

class WithdrawalRequestForm(forms.ModelForm):
    class Meta:
        model = WithdrawalRequest
        fields = ['amount']