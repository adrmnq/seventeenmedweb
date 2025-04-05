from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('member', views.member),
    path('form', views.form),
    path('academic', views.academic)
]