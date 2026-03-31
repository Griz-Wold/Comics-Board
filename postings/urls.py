from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('create_posting/', views.create_posting, name='create_posting'),
    path('post/<int:id>/', views.posting_detail, name='posting_detail'),
    path('delete/<int:id>/', views.delete_posting, name='delete_posting'),
    path('edit/<int:id>/', views.edit_posting, name='edit_posting'),
]