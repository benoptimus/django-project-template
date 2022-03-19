#!/usr/bin/env python
#-*- coding: utf-8 -*-


from django.urls import include, re_path, path
from rest_framework import routers

from api.views import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', UserViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
