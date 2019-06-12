"""rest_framwork URL Configuration

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
from app01 import views

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

from app01.views import SnippetViewSet, UserViewSet
# from app01.views api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

#coreapi
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='Pastebin API')


#最终简化版
# Create a router and register our viewsets with it.
router = DefaultRouter()  #自动创建api_root
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),
    url(r'^report_builder/', include('report_builder.urls')),
]

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')
#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

#用viewset之后 替换成如下模式
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = format_suffix_patterns([
#     url(r'^$', api_root),
#     url(r'^snippets/$', snippet_list, name='snippet-list'), #注意后面name是供api-root调用
#     url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
# ])

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # url(r'^', include(router.urls)),
#     url(r'^$', views.api_root),
#
#     # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url(r'^users/$', views.UserList.as_view(), name='user-list'),  #用户权限管理
#
#     url(r'^authmanager/', include('rest_framework.urls')),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
#
#     url(r'^index/$', views.index),
#     url(r'^snippet_list/$', views.snippet_list), #rest函数视图
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
#
#     url(r'^snippnet_class/$', views.SnippetList.as_view()), #rest类视图
#     url(r'^snippnet_class/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
#
#     url(r'^snippnet_class_mixin/$', views.SnippetList_mixin.as_view()), #rest mixin类视图
#     url(r'^snippnet_class_mixin/(?P<pk>[0-9]+)/$', views.SnippetDetail_mixin.as_view()),
#
#     url(r'^snippnet_class_generics/$', views.SnippetList_generics.as_view(), name='snippet-list'), #终极版 generics类视图
#     url(r'^snippnet_class_generics/(?P<pk>[0-9]+)/$', views.SnippetDetail_generics.as_view(), name='snippet-detail'),
#     url(r'^snippnet_class_generics/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

