#!/usr/bin/env python
#-*- coding: utf-8 -*-


from rest_framework import serializers

from cuser.models import User

import datetime
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password','activation_key',
                   'groups','user_permissions','is_superuser',
                   'is_staff',
                )