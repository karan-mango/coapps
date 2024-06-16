# myapp/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='dashboard'), name='logout'),
    path('new-employee/', views.new_employee, name='new_employee'),
    # Add other URLs as needed
]
