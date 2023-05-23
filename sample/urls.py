"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from sampleapp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('circle/',views.circle, name='circle'),
    path('rectangle/',views.rectangle, name='rectangle'),
    path('triangle/',views.triangle, name='triangle'),
    path('sphere/',views.sphere, name='sphere'),
    path('frustrum/',views.frustrum,name='frustrum'),
    path('admin/', admin.site.urls),
]
