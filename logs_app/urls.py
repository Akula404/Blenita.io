from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = 'logs_app'

urlpatterns = [
    path('register_client/', views.register_client, name = "register_client"),
    path('login_client', views.login_client, name = "login_client"),

        # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'), name='password_reset'),
    
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    path('logout_view/', views.logout_view, name='logout_view'),
]