"""
URL configuration for destiny_church project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


site_name = "Distiny Church"


urlpatterns = [
    path('', include('authentication.urls'), name='authentication'),
    path('', include('offerings_management.urls'), name='offerings_management'),
    path('', include('members_management.urls'), name='members_management'),
    path('', include('visitos_management.urls'), name='visitos_management'),
    path('', include('management_panel.urls'), name='management_panel'),
    path('admin/', admin.site.urls),
]
