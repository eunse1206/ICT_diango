"""
URL configuration for ohyun_highschool project.

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
from main.views import index, jejuohyun, high_1st, high_2nd, high_3rd, my_page, grade

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('jejuohyun/', jejuohyun),
    path('1st/', high_1st),
    path('2nd/', high_2nd),
    path('3rd/', high_3rd),
    path('my_page/', my_page),
    path('grade/', grade),
]
