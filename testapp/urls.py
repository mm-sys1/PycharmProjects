from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('list/', views.post_list, name='post_list'),
    path('test/', views.create_post, name='create_post'),
]
