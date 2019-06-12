from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^django_form/$', views.django_form),
    url(r'^form2/$', views.form2),
    url(r'^select_test/$', views.select_test),
]