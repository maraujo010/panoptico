from django.conf.urls import patterns, include, url

urlpatterns = patterns('',    
    url(r'^', include('panoptico.apps.webApp.urls')),

)
