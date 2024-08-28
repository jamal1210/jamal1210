from django import forms
from django.core import validators

#creat a personal forms

class personal_info (forms.Form):
    password = forms.CharField(widget=forms.PasswordInput,min_length=6)
    re_password = forms.CharField(widget=forms.PasswordInput,min_length=6)


    def clean(self):
        frm = super().clean()
        passw_match = self.cleaned_data['password']
        re_passw_match = self.cleaned_data['re_password']
        if passw_match != re_passw_match:
           raise forms.ValidationError('password does,t match') 