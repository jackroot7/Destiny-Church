from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views import View
from utils.Config import SysConfigs
from utils.utils import get_message

class AuthenticationView(View):
    def get(self, request, **kwargs):
        if request.htmx:
            return render(request, 'views/auth/login.html')
        else:
            return render(request, 'views/auth/login.html')

    def post(self, request, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            get_message(request, message = 'You have successfully login'+str(user.first_name), type="success", title='Welcome')
            return redirect("/")
        else:
            get_message(request, 'Invalid username or password.')
        return redirect("/login")

class LogoutView(View):
    def get(self, request, **kwargs):
        logout(request)
        return redirect("/login")

class RegistrationView(View):
    def get(self, request, **kwargs):
        if request.htmx:
            return render(request, 'views/auth/register.html', {'config':SysConfigs.get_configs()})
        else:
            return render(request, 'views/auth/register.html', {'config':SysConfigs.get_configs()})

class ResetPasswordView(View):
    def get(self, request, **kwargs):
        if request.htmx:
            return render(request, 'views/auth/forgot.html')
        else:
            return render(request, 'views/auth/forgot.html')


