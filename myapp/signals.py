# myapp/signals.py
from django.contrib.auth.models import User as AuthUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import User

@receiver(post_save, sender=AuthUser)
def create_custom_user(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        custom_user = User(
            name=instance.username,  # Assuming the name is the same as username for simplicity
            username=instance.username,
            password=instance.password,  # It's stored as a hash
            is_employee=False,  # Set based on your logic
            is_admin=True
        )
        custom_user.save()
