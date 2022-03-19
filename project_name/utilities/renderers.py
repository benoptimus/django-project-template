#!/usr/bin/env python
#-*- coding: utf-8 -*-


from email import message
from rest_framework.renderers import BaseRenderer
from rest_framework.utils import json
from rest_framework.views import exception_handler
from rest_framework.renderers import JSONRenderer
from rest_framework import exceptions
from rest_framework.utils.serializer_helpers import ReturnList

from utilities.codes import CodeMessage
class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        if isinstance(data, ReturnList):
             response = {
                "code": CodeMessage.SUCCESSFULL,
                "data": data,
                "message": "success"
            }
        else:
            code = data.pop('code', status_code)
            response = {
                "code": code,
                "data": data,
                "message": data.pop("description", data.pop('detail', CodeMessage.messages.get(code, None)))
            }
        if not str(status_code).startswith('2'):
            response["data"] = data
        return super(CustomRenderer, self).render(response, accepted_media_type, renderer_context)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        if isinstance(exc, exceptions.ValidationError) and isinstance(response.data.get('code',400), int):
            response.data.update({'code': CodeMessage.BAD_REQUEST})
        if isinstance(exc, exceptions.AuthenticationFailed):
            response.data.update({'code': CodeMessage.UNAUTHORIZED})
        # elif isinstance(exc, exceptions.MethodNotAllowed):
        #     response.data.update({'code': CodeMessage.UNAUTHORIZED})
        # elif isinstance(exc, exceptions.NotAcceptable):
        #     response.data.update({'code': CodeMessage.UNAUTHORIZED})
        elif isinstance(exc, exceptions.NotAuthenticated):
            response.data.update({'code': CodeMessage.UNAUTHORIZED})
        # elif isinstance(exc, exceptions.NotFound):
        #     response.data.update({'code': CodeMessage.UNAUTHORIZED})
        # elif isinstance(exc, exceptions.ParseError):
        #     response.data.update({'code': CodeMessage.UNAUTHORIZED})
        # elif isinstance(exc, exceptions.PermissionDenied):
        #     response.data.update({'code': CodeMessage.UNAUTHORIZED})
        # elif isinstance(exc, exceptions.Throttled):
        #     response.data.update({'code': CodeMessage.UNAUTHORIZED})
        # elif isinstance(exc, exceptions.UnsupportedMediaType):
        #     response.data.update({'code': CodeMessage.UNAUTHORIZED})
        # elif isinstance(exc, exceptions.ValidationError):
        #     response.data.update({'code': CodeMessage.UNAUTHORIZED})

    return response
