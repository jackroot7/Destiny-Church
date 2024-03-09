from django.shortcuts import render
from django.views import View
from utils.Config import SysConfigs

class AuthenticationView(View):
    def get(self, request, **kwargs):
        if request.htmx:
            return render(request, 'views/auth/login.html')
        else:
            return render(request, 'views/auth/login.html')

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


