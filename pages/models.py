from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user model for default user details
    and order history
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, blank=True, default='')
    default_street_address1 = models.CharField(max_length=80, blank=True, default='')
    default_street_address2 = models.CharField(max_length=80, blank=True, default='')
    default_town_or_city = models.CharField(max_length=40, blank=True, default='')
    default_county = models.CharField(max_length=80, blank=True, default='')
    default_postcode = models.CharField(max_length=20, blank=True, default='')
    default_country = CountryField(blank_label="Country", blank=True, default='')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update user profile
    """

    if created:
        UserProfile.objects.create(user=instance)
    # save on update
    instance.userprofile.save()


class Faq(models.Model):
    """
    A model for Frequently asked questions items
    """

    collapse_id = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=150, null=False, blank=False)
    body = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title
