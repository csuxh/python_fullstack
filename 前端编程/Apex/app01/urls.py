from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^add_user/', views.add_user),
    url(r'^user_list/', views.user_list),
    url(r'^publisher_list/', views.publisher_list),
    url(r'^add_publisher/', views.add_publisher),
    url(r'^delete_publisher/', views.delete_publisher),
    url(r'^edit_publisher/', views.edit_publisher),
    url(r'^book_list/', views.book_list),
    url(r'^add_books/', views.add_books),
    url(r'^delete_book/', views.delete_book),
    url(r'^edit_books/', views.edit_books),

    url(r'^template_test', views.template_test),
    url(r'^test', views.test),
    url(r'^upload/', views.upload),
    url(r'^json_test/', views.json_test),
]
