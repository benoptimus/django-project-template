#!/usr/bin/env python
#-*- coding: utf-8 -*-


from rest_framework import exceptions

class ServiceUnavailableException(exceptions.APIException):
    def __init__(self, message, code=503):

        # Call the base class constructor with the parameters it needs
        super(ServiceUnavailableException, self).__init__(message)
        # Now for your custom code...
        status_code = 504
        message = 'Service unavailable'
        default_code = 'service_unavailable'

class ServiceUnavailableException1(exceptions.NotAuthenticated):
    def __init__(self, message, code=503):

        # Call the base class constructor with the parameters it needs
        super(ServiceUnavailableException1, self).__init__(message)
        # Now for your custom code...
        code = 504
        message = 'Service unavailable'
        default_code = 'service_unavailable'
