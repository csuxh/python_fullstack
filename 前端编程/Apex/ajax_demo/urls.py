from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^login/$', views.login_page ),
    url(r'^user_list/', views.user_list ),
    url('^ajax_test/$', views.ajax_test),
    url('^ajax_add/', views.ajax_add),
    url('^list/', views.page_list),
]