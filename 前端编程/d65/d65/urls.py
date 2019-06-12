"""d65 URL Configuration

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
# from django.contrib import admin
from django.urls import path
from app1 import views, urls
from app2 import views as app2_view
from app03 import views as v3
from app03 import urls as u3


from django.conf.urls import url, include
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
urlpatterns = [
    # url(r'^publisher_list/', views.publisher_list),
    # url(r'^delete_publisher/$', views.delete_publisher),
    # url(r'^delete_publisher/([0-9]+)/$', views.delete_publisher2),

    url(r'^app1/', include(urls) ),
    # url(r'^app03/login/$', v3.login ),
    url(r'^app03/', include(u3) ),
    url(r'^app03/home/$', v3.home )
]

