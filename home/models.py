# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    user1 = models.TextField(max_length=255, null=True, blank=True)
    user2 = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Apple(models.Model):

    #__Apple_FIELDS__
    aplle fruit = models.TextField(max_length=255, null=True, blank=True)
    apple fruit = models.TextField(max_length=255, null=True, blank=True)
    test = models.TextField(max_length=255, null=True, blank=True)

    #__Apple_FIELDS__END

    class Meta:
        verbose_name        = _("Apple")
        verbose_name_plural = _("Apple")



#__MODELS__END
