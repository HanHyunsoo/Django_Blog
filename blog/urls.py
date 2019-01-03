# 주석 친 코드는 Django 2.0 미만에서 쓰는 코드
# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    path('', views.post_list, name='post_list'), # = /
    path('post/<pk>/', views.post_detail, name='post_detail'),
]