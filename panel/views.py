from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Customer
from django.views import View
# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, 'signup.html')
