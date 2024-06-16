# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from .models import User
from django.contrib.auth.hashers import check_password  # Import Django's password checking function
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



from .decorators import custom_login_required
from .forms import EmployeeForm

@custom_login_required
def new_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Create a new User instance but don't save it yet
            user = form.save(commit=False)
            # Set password (using set_password() method if using a custom password hashing mechanism)
            user.set_password(form.cleaned_data['password'])
            # Save the user object
            user.save()
            # Redirect to a success page or admin dashboard
            return redirect('dashboard')  # Adjust 'dashboard' to your actual admin dashboard URL name
    else:
        form = EmployeeForm()
    
    return render(request, 'myapp/new_employee.html', {'form': form})
# @custom_login_required

@custom_login_required
def dashboard(request):
    is_admin = request.session.get('is_admin', False)
    context = {
        'is_admin': is_admin,
    }
    return render(request, 'myapp/dash.html', context)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(username=username)
                
                # Check if the entered password matches the stored hashed password
                if check_password(password, user.password)or password==user.password:
                    # Passwords match, proceed with login
                    request.session['username'] = user.username
                    if user.is_admin:
                        request.session['is_admin'] = 1  # Admin user
                    else:
                        request.session['is_admin'] = 0  # Employee user
                    messages.success(request, 'Login successful.')
                    return redirect('dashboard')  # Replace 'dashboard' with your desired redirect URL after login
                else:
                    # Passwords do not match
                    messages.error(request, 'Invalid username or password.')
            except User.DoesNotExist:
                # User does not exist
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'myapp/login.html', {'form': form})



