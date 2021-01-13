from django.contrib import admin
from django.urls import path
from .views import Home, Signup, Login, Logout


urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('signup', Signup.as_view(), name="signup"),
    path('login', Login.as_view(), name="login"),
    path('logout', Logout.as_view(), name="logout")
]
