# myapp/forms.py
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


# myapp/forms.py
from django import forms
from .models import User

class EmployeeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    is_admin = forms.BooleanField(label='Is Admin', required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'is_admin']
