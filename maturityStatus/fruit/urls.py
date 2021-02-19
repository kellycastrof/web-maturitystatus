  
from django.urls import path
from fruit.views import Home, about_us
from rest_framework.authtoken import views

urlpatterns = [
    path('', Home.as_view()),
    
]