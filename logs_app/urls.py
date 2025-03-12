from django.urls import path  
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
    register_client,
    login_client,
    logout_view
)  

app_name = 'logs_app'  

urlpatterns = [
    path('register_client/', register_client, name="register_client"),  
    path('login_client/', login_client, name="login_client"),  

    # ✅ Use custom views instead of Django's default views  
    path('reset_password/', CustomPasswordResetView.as_view(), name="reset_password"),  

    path('reset_password_done/', CustomPasswordResetDoneView.as_view(), name="password_reset_done"),  

    path('reset_password_confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),  

    path('reset_password_complete/', CustomPasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('logout_view/', logout_view, name='logout_view'),  
]  
