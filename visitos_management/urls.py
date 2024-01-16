
from django.contrib import admin
from django.urls import include, path
from visitos_management.views import *

urlpatterns = [
    path('visitors', VisitorsView.as_view(), name='visitors'),
    path('visitors/<uuid:action_id>/', VisitorsView.as_view(), name='visitors'),
    path('visitor_sms_notification', VisitorsNotificationsView.as_view(), name='visitor_sms_notification'),
]