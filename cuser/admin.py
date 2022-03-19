#!/usr/bin/env python
#-*- coding: utf-8 -*-


from cuser.models import User

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from utilities.helpers import CustomModelAdmin
@admin.register(User)
class UserAdmin(BaseUserAdmin, CustomModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone', 'profile_photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('username','email', 'first_name', 'last_name', 'is_staff', 'type_entity')
    search_fields = ('email', 'first_name', 'last_name')
    exclude_fields = ['password']
    ordering = ('email',)
