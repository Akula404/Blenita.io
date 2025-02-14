from django.urls import path
from .import views

app_name = 'logs_app'

urlpatterns = [
    path('register_client/', views.register_client, name = "register_client"),
    path('login_client', views.login_client, name = "login_client"),
    path('logout_view/', views.logout_view, name='logout_view'),
]