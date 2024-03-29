from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def creat_profile(instance, created, *args, **kwargs):  # receiver must and should have *args and *kwargs
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(instance, created, *args, **kwargs ):
    instance.profile.save()
