from django.urls import path,re_path
from .views import *
urlpatterns = [
    path('login/',login),
    path('register/',register),
    path('index/',index),
    path('logout/',logout),
    # path('goods/',goods),
    re_path('goods/(?P<page>\d+)/(?P<status>\d+)/',goods),
    re_path('goods_status/(?P<id>\d+)/(?P<status>\w+)/',goods_status),
    path('user_profile/',user_profile),
    path('goods_add/',goods_add),
    path('add_label/',add_label),

]