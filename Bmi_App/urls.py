from django.urls import path
from . import views

urlpatterns = [
     path('',views.home,name="home"),
     path('result/',views.result,name="result"),
     path('check-bmi/',views.check_bmi,name="check_bmi"),
     path('aboutBmi',views.about,name="about"),
    
    
     
    
    
]