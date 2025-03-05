from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


# Create your views here.

# Register View

def register_client(request):
    """Registration view with auto-login after successful registration"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Authenticate the user
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)  # Auto-login after registration

                    messages.success(request, "Account created successfully! You are now logged in.")

                    # Redirect to 'next' page if it exists, else to home
                    next_page = request.GET.get('next', 'restaurant_app:home')
                    return redirect(next_page)
                else:
                    messages.error(request, "Error logging in after registration. Please log in manually.")
                    return redirect('logs_app:login_client')

            except Exception as e:
                messages.error(request, f"Registration failed: {str(e)}")
        else:
            messages.error(request, "Passwords do not match. Please try again.")

    return render(request, 'accounts/register_client.html')

# Login View

def login_client(request):
    """Login view with redirect to next page if provided"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")

            # Redirect to 'next' page if exists, else to home
            next_page = request.GET.get('next', 'restaurant_app:home')
            return redirect(next_page)
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'accounts/login_client.html')



class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_sent')


class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_sent.html'


class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('password_reset_complete')


class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_done.html'




def logout_view(request):
    """ This is for the logout view"""
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('restaurant_app:home')





