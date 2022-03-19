#!/usr/bin/env python
#-*- coding: utf-8 -*-


from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

from django_countries.fields import CountryField
from django.contrib.sites.models import Site
from model_utils import FieldTracker

from utilities.choices import  IDTypeCard
from utilities.fields import CharNullField

import re
import os

SHA256_RE = re.compile('^[a-f0-9]{40,64}$')

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.user.id, instance.username, ext)
    return os.path.join('uploads', filename)

class User(AbstractUser):
    title = models.CharField(max_length=5, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)

    email = models.EmailField(unique=True, null=False, blank=False)
    phone = CharNullField(unique=True, max_length=20, null=True, blank=True)

    identity_id_number = models.CharField(max_length=20, blank=True, null=True)
    identity_type = models.CharField(max_length=20, blank=True, null=True, choices=IDTypeCard.CHOICES)
    identity_photo_verso = models.ImageField(upload_to=content_file_name, blank=True, null=True)
    identity_photo_recto = models.ImageField(upload_to=content_file_name, blank=True, null=True)

    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    activation_key =  models.CharField(max_length=255, blank=True, null=True)

    identity_verified = models.BooleanField(default=False)
    profile_photo = models.ImageField(upload_to=content_file_name, blank=True, null=True)

    class Meta:
        verbose_name = _('Utilisateur')

    def __str__(self):
        if self.email:
            return self.email
        else:
            return self.username

    def __unicode__(self):
        if self.email:
            return self.email
        else:
            return self.username
    tracker = FieldTracker()
