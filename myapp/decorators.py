# decorators.py
from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse

def custom_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Check if user is authenticated based on your custom logic
        if 'username' in request.session:
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse('login'))  # Redirect to login page if not authenticated
    
    return wrapper


def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Check if user is authenticated and admin based on session variable
        if request.session.get('is_admin') == 1:
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to unauthorized page or handle accordingly
            return redirect(reverse('dashboard'))  # Redirect to dashboard or other page
    
    return wrapper
