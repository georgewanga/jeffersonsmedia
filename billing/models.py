from decimal import Decimal
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from products.models import Product

User = settings.AUTH_USER_MODEL

class BillingProfile(models.Model):
    user = models.OneToOneField(User, on_delete=None, null=True, blank=True)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name_plural = "BillingProfile"


# def billing_profile_created_receiver(sender,instance,created,*args,**kwargs):
#     if created:
        

def user_created_receiver(sender,instance,created,*args,**kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)
    
post_save.connect(user_created_receiver,sender=User)
