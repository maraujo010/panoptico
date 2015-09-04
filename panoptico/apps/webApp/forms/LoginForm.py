# coding=utf8

from django import forms
from CustomForm import CustomForm

class LoginForm(CustomForm):
    
    email_errors = {
    'required': CustomForm.validation_errors['INAVLID_EMAIL'],
    'invalid': CustomForm.validation_errors['INAVLID_EMAIL'],
    }
         
    username_errors = {
    'required': CustomForm.validation_errors['PASSWORD_REQUIRED'],    
    }         
         
    email = forms.EmailField(error_messages=email_errors, initial='email...')
    password = forms.CharField(error_messages=username_errors, widget=forms.PasswordInput())
    


    
 