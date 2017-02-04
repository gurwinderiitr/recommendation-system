from django.contrib.auth.forms import AuthenticationForm 
from django import forms


import re
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs={'max_length': 30, 'required': True, 'class': 'form-control', 'name': 'username'}), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs={'max_length': 30, 'required': True, 'class': 'form-control', 'name': 'email'}), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'max_length': 30, 'render_value': False, 'required': True, 'class': 'form-control', 'name': 'password'}), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'max_length': 30, 'render_value': False, 'required': True, 'class': 'form-control', 'name': 'password'}), label=_("Password (again)"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
