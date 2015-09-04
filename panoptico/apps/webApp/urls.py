from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'),
    url(r'^login/', views.iniciarSessao, name='login'),
    url(r'^logout/', views.terminarSessao, name='login'),
    url(r'^registar/', views.registar, name='resgistar'),
    url(r'^userAccount/', views.userAccount, name="userAccount"),
    url(r'^contacto/', views.contacto, name="contacto"),
    url(r'^apoia/', views.apoia, name="apoia"),
    url(r'^participa/', views.participa, name="participa"),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^androidApp/', views.androidApp, name='androidApp'),
    url(r'^estatisticas/', views.estatisticas, name='estatisticas'),
    url(r'^sobre/', views.sobre, name='sobre'),
    url(r'^admin/', include(admin.site.urls)),
)
