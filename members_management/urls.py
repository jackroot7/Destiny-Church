
from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('members', MembersView.as_view(), name='members'),
    path('members/<uuid:action_id>/', MembersView.as_view(), name='members'),
    path('childrens', ChildrensView.as_view(), name='childrens'),
]