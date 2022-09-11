from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            email=user.email,
            name=user.username
        )


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
