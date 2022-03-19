#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django.utils.translation import gettext_lazy as _

class Gender:
    M, F = ('MALE', 'FEMALE')
    CHOICES = (
            (M, 'Male'),
            (F, 'Female'),
        )

class IDTypeCard:
    PP, LD, NCD = ('PASSPORT', 'LICENSEDRIVER', 'NATIONALCARD')
    CHOICES = (
            (PP, 'Passport'),
            (LD, 'License Driver'),
            (NCD, 'National Card'),
        )
