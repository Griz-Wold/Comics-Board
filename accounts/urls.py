from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create_account/', views.create_account, name='create_account'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='mainpage'), name='logout'),
    path('account/', views.account, name='account'),
]