from django.urls import path, re_path
from . import views

urlpatterns = [
    # re_path('^$', views.home, name='home'),
    re_path('^$', views.HomeIndex.as_view(), name='home'),
    re_path('^counters/$', views.CounterIndexWithTitle.as_view(), name='counter'),
    re_path('^products/(?P<pk>.+)/$', views.ProductItemWithOther.as_view(), name='product_item'),

    re_path('^transformators/$', views.TransformatorIndexWithTitle.as_view(), name='transformator'),
    re_path('^boards/$', views.BoardIndexWithTitle.as_view(), name='board'),
    re_path('index/$', views.index, name='index'),
    re_path('column/$', views.column, name='column'),
    re_path('group/$', views.group, name='group'),
    re_path('^product/(?P<name>.+)/$', views.product, name='product'),
    re_path('parser/$', views.parser, name='parser'),
]
