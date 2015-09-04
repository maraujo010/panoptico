# coding=utf8

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from forms.LoginForm import LoginForm
from forms.RegistrationForm import RegistrationForm
from viewHelpers.userAccountViewHelper import *
from django.http import HttpResponseRedirect


""" página inicial """
def index(request):
    data = {'menu1Se1ect1' : 'mainMenuMapaSelected'}
    
    return render(request, 'mapa.tpl', data)


""" sobre """
def sobre(request):
    data = {'menu2Se1ect1' : 'class=menuOpcSelected'}
    
    return render(request, 'sobre.tpl', data)


""" blog """
def blog(request):
    data = {'menu1Se1ect2' : 'mainMenuBlogSelected'}
    
    return render(request, 'blog.tpl', data)


""" android app """
def androidApp(request):
    data = {'menu1Se1ect3' : 'mainMenuAppSelected'}
    
    return render(request, 'androidApp.tpl', data)


""" estatisticas """
def estatisticas(request):
    data = {'menu1Se1ect4' : 'mainMenuEstatisticasSelected'}
    
    return render(request, 'estatisticas.tpl', data)


""" login """
def iniciarSessao(request):
    
    data = {}
    
    if request.method == 'POST':
        
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email=request.POST.get('email')
            password=request.POST.get('password')
            user = authenticate(email=email, password=password)
        
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/userAccount/")
                else:
                    data['failedLogin']=form.validation_errors['LOGIN_ERROR_2']
                    form = LoginForm(label_suffix='')
            else:    
                data['failedLogin']=form.validation_errors['LOGIN_ERROR_1']
                form = LoginForm(label_suffix='')
    
    else:
        form = LoginForm(label_suffix='')
    
    data['menu0Se1ect1'] = 'class=menuOpcSelected'
    data['form'] = form
    
    return render(request, 'login.tpl', data)


''' logout '''
def terminarSessao(request):
    logout(request)
    return HttpResponseRedirect("/")
    


""" área do utilizador """
def userAccount(request):
    data = userAccountViewHelper(request)
    
    return render(request, 'userAccount.tpl', data)


""" registo """
def registar(request):    
    
    data = {}
    
    if request.method == 'POST':        
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            email=request.POST.get('email')
    
    else:
        form = RegistrationForm(label_suffix='')
    
    data['menu0Se1ect2'] = 'class=menuOpcSelected'
    data['form'] = form
        
    return render(request, 'registar.tpl', data)


""" contacto """
def contacto(request):
    data = {'menu2Se1ect4' : 'class=menuOpcSelected'}
    
    return render(request, 'contacto.tpl', data)


""" apoia """
def apoia(request):
    data = {'menu2Se1ect3' : 'class=menuOpcSelected'}
    
    return render(request, 'contacto.tpl', data)


""" participa """
def participa(request):
    data = {'menu2Se1ect2' : 'class=menuOpcSelected'}
    
    return render(request, 'participa.tpl', data)

