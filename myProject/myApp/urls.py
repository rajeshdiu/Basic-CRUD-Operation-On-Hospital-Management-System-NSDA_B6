
from django.contrib import admin
from django.urls import path,include
from myApp.views import *


urlpatterns = [
    path('',homePage,name="homePage"),
    path('doctorPage/',doctorPage,name="doctorPage"),
    path('patientPage/',patientPage,name="patientPage"),
    path('appointmentPage/',appointmentPage,name="appointmentPage"),
    path('departmentPage/',departmentPage,name="departmentPage"),
    
    
    path('DoctordeletePage/<int:id>',DoctordeletePage,name="DoctordeletePage"),
    path('DoctoreditPage/<int:id>',DoctoreditPage,name="DoctoreditPage"),
    
    
]
