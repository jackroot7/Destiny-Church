
from django.contrib import admin
from django.urls import include, path
from management_panel.views import *

urlpatterns = [
    path('', view=home, name='home'),
    path('forms/', view=forms, name='forms'),
    path('users', view=users_list, name='users'),
]