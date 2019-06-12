from django.conf.urls import url
# from . import views
from app1 import views

urlpatterns = [
    url(r'^home/', views.home, {"age": 18}, name="home"),
    # 位置参数
    # url(r'^book/([0-9]{2,4})/([a-zA-Z]{2})/$', views.book, name="book"),
    # 关键字参数
    # url(r'^book/(?P<year>[0-9]{2,4})/(?P<title>[a-zA-Z]{2})/$', views.book, name="book")
    url(r'^book/(?P<year>[0-9]{2,4})/(?P<title>[a-zA-Z]{2})/$', views.book)

]