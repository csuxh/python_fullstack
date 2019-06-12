"""Apex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url, include
from app01 import urls as u1
from ajax_demo import urls as u2
from ajax_demo import views as v2
from d73_forms import urls as u3

#
urlpatterns = [
    url(r'^app01/', include(u1)),
    url(r'^ajax_demo/', include(u2)),
    url(r'^d73_forms/', include(u3)),
    url(r'^index/', v2.index),
    url(r'^login/$', v2.login_page),
    path('admin/', admin.site.urls),
]

