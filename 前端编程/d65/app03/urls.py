from django.conf.urls import url
from . import views
# from app03 import views

urlpatterns = [
    url(r'^login/', views.login ),
]