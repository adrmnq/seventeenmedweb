from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index),
    path('member', views.member),
    path('form', views.form),
    path('academic', views.academic),
    
    path('login', views.login),
    path('account/', include('allauth.urls'))
]