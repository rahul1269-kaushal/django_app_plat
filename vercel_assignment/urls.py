"""
URL configuration for vercel_assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from vercel_assignment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('1/', views.q1),
    path('2/', views.q2),
    path('3/', views.q3),
    path('4/', views.q4),
    path('5/', views.q5),
    path('6/', views.q6),
    path('7/', views.q7),
    path('8/', views.q8),
    path('9/', views.q9),
    path('10/', views.q10),
]
