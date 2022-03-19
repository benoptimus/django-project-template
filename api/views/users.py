#!/usr/bin/env python
#-*- coding: utf-8 -*-


from rest_framework import viewsets, mixins

from cuser.models import User
from utilities.permissions import CreateAndIsAuthenticated

from api.serializers.users import UserSerializer

class UserViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User.objects.none()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put']
    permission_classes = (CreateAndIsAuthenticated,)
