from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import Profile


User=settings.AUTH_USER_MODEL
@receiver(post_save, sender=User)
def create_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)