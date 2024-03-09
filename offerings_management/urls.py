
from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('offerings', OfferingsView.as_view(), name='offerings'),
    path('tenths_list', TenthsManagementView.as_view(), name='tenths_list'),
]