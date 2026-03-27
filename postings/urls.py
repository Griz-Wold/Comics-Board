from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('create_posting/', views.create_posting, name='create_posting'),
]