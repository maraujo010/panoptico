# coding=utf8

from django import forms

class CustomForm(forms.Form):
    validation_errors = {'INAVLID_EMAIL' : 'Introduz um email válido',
                         'PASSWORD_REQUIRED' : 'Introduz uma password',
                         'LOGIN_ERROR_1' : 'Email ou password inválida',
                         'LOGIN_ERROR_2' : 'Utilizador inactivo'}