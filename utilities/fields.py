#!/usr/bin/env python
#-*- coding: utf-8 -*-


from django.db import models

class CharNullField(models.CharField):
    description = "CharField that stores NULL"
    def get_db_prep_value(self, value, connection=None, prepared=False):
        value = super(CharNullField, self).get_db_prep_value(value, connection, prepared)
        if value=="":
            return None
        else:
            return value
