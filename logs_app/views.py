from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
# Create your views here.

# Register View
def register_client(request):
    """Registration view"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Notify user and redirect to login page
                messages.success(request, "Account created successfully! Please log in.")
                return redirect('logs_app:login_client')
            except Exception as e:
                messages.error(request, f"Registration failed: {str(e)}")
        else:
            messages.error(request, "Passwords do not match. Please try again.")

    return render(request, 'accounts/register_client.html')


# Login View
def login_client(request):
    """Login view"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect("restaurant_app:home")  # Adjust this redirect as needed
        else:
            messages.error(request, "Invalid login credentials")
    return render(request, 'accounts/login_client.html')


# Password Reset Views
class CustomPasswordResetView(PasswordResetView):
    template_name = "accounts/password_reset.html"
    email_template_name = "accounts/password_reset_email.html"
    success_url = reverse_lazy("logs_app:password_reset_done")

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy("logs_app:password_reset_complete")

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"


def logout_view(request):
    """ This is for the logout view"""
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('restaurant_app:home')





