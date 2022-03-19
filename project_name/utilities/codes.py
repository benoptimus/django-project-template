
#!/usr/bin/env python
#-*- coding: utf-8 -*-

class CodeMessage:
    SUCCESSFULL = '0000'
    BAD_REQUEST = '4000'
    UNAUTHORIZED = '4010'
    ACTIVATION_FAILED = '4110'
    RESEND_ACTIVATION_FAILED = '4120'


    messages = {
        SUCCESSFULL: 'success',
        BAD_REQUEST: 'Bad request',
        ACTIVATION_FAILED: 'Activation key not correct or expired',
        RESEND_ACTIVATION_FAILED: 'Activation key not sent'
    }
