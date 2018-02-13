from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^$', views.home, name='home'),
    re_path('index/$', views.index, name='index'),
    re_path('column/$', views.column, name='column'),
    re_path('group/$', views.group, name='group'),
    re_path('^product/(?P<name>.+)/$', views.product, name='product'),
    re_path('parser/$', views.parser, name='parser'),
]
