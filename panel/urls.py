from django.contrib import admin
from django.urls import path
from .views import Home, Signup

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('signup', Signup.as_view(), name="signup")
]
