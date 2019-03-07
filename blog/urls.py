from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    # path('new/', views.new, name='new'),
    # path('create/', views.create, name='create'),
    path('post_new/', views.post_new, name='post_new'),
    path('post_edit/<int:pk>', views.post_edit, name='post_edit'),
    path('post_remove/<int:pk>', views.post_remove, name='post_remove')
]