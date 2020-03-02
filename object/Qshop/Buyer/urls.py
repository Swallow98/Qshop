from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('index/',index),
    path('login/',login),
    path('register/',register),
    path('goods_list/',goods_list),
    path('goods_detail/',goods_detail),
    # re_path('goods_detail/\w/(?P<page>\d+)/',goods_detail),
    path('goods_place_order/',goods_place_order),

]