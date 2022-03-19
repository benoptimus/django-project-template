#!/usr/bin/env python
#-*- coding: utf-8 -*-


from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema

class CreateAndIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            if view.action in ['create', 'authenticate','activate', 'resend_activation_key']:
                return True
            else:
                return False
        else:
            return True
