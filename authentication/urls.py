from django.urls import path
from .views import *

urlpatterns = [
    path('login', AuthenticationView.as_view(), name='login'),
    path('register', RegistrationView.as_view(), name='register'),
    path('forgot-password', ResetPasswordView.as_view(), name='forgot-password'),
]