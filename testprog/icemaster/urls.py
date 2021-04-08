from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name = 'home'),
    path('first_ice_cream',views.first_ice_cream, name='choco'),
    path('second_ice_cream',views.second_ice_cream, name='vanil'),
    path('third_ice_cream',views.third_ice_cream, name='cherry'),
]

