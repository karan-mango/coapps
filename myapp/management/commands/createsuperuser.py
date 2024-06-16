# myapp/management/commands/createsuperuser.py
from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from django.core.management.base import CommandError

class Command(BaseCommand):
    help = 'Create a superuser with additional fields.'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        
        username = input('Username: ')
        if User.objects.filter(username=username).exists():
            raise CommandError('Error: That username is already taken.')
        
        password = input('Password: ')
        name = input('Name: ')
        is_employee = input('Is Employee (yes/no): ').strip().lower() == 'yes'
        
        user = User.objects.create_superuser(
            username=username,
            password=password,
            name=name,
            is_employee=is_employee
        )
        
        self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully'))
