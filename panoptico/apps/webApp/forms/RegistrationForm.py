# coding=utf8

from django import forms
from CustomForm import CustomForm
from django.core.mail import send_mail

class RegistrationForm(CustomForm):
    
    email_errors = {
    'required': CustomForm.validation_errors['INAVLID_EMAIL'],
    'invalid': CustomForm.validation_errors['INAVLID_EMAIL'],
    }
         
    username_errors = {
    'required': CustomForm.validation_errors['PASSWORD_REQUIRED'],    
    }         
         
    username = forms.CharField(error_messages=username_errors)
    email = forms.EmailField(error_messages=email_errors)
    password = forms.CharField(error_messages=username_errors, widget=forms.PasswordInput())
    confirm_password = forms.CharField(error_messages=username_errors, widget=forms.PasswordInput())
    


    
 