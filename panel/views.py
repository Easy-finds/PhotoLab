from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Customer, UploadImages
from django.views import View
# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        return render(request, 'home.html')


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        customer = Customer(first_name=postData.get('name'),
                            last_name=postData.get('sirname'),
                            mobile=postData.get('mobile'),
                            email=postData.get('email'),
                            password=postData.get('password'))

        error_message = self.Validate(customer)

        if error_message:
            values = {
                'name': customer.first_name,
                'sirname': customer.last_name,
                'mobile': customer.mobile,
                'email': customer.email
            }
            data = {'error': error_message, 'values': values}
            return render(request, 'signup.html', data)
        else:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('home')

    def Validate(self, customer):
        error_message = None

        if not customer.first_name:
            error_message = 'First name required!!'
        elif len(customer.first_name) < 3:
            error_message = 'Length of name must be 3 character or more'
        elif not customer.last_name:
            error_message = 'Last name required!!'
        elif len(customer.last_name) < 3:
            error_message = 'Length of last name must be 3 character or more'
        elif not customer.email:
            error_message = 'Email required!!'
        elif customer.isExists():
            error_message = 'Email already registered'
        else:
            error_message = None
        return error_message


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        print(Login.return_url)
        return render(request, 'login.html')

    def post(self, request):
        login = request.POST
        customer = Customer.checkUser(login.get('email'))
        if customer:
            if check_password(login.get('password'), customer.password):
                request.session['customer'] = customer.id
                print(Login.return_url)
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('home')
            else:
                error_message = 'Incorrect Password!!'
                data = {'error': error_message, 'email': customer.email}
                return render(request, 'login.html', data)
        else:
            return render(request, 'login.html', {'error': 'Email not found'})


class Logout(View):
    def get(self, request):
        print(request.session.get('customer'))
        request.session['customer'] = {}
        return redirect('home')
