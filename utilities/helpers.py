#!/usr/bin/env python
#-*- coding: utf-8 -*-


from django.contrib import admin
from rest_framework import serializers
from rest_framework.exceptions import ErrorDetail, ValidationError
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

from django.core.exceptions import ImproperlyConfigured
from os import environ

from utilities.codes import CodeMessage
class CustomModelAdmin(admin.ModelAdmin):
    exclude_fields = []

    def __init__(self, model, admin_site):
        self.list_display += tuple([field.name for field in model._meta.fields if field.name not in self.exclude_fields])
        super(CustomModelAdmin, self).__init__(model, admin_site)

class ReadOnlyModelSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        for field in fields:
            fields[field].read_only = True
        return fields

class MySerializers(serializers.Serializer):
    def is_valid(self, raise_exception=False, code=CodeMessage.BAD_REQUEST, error_description=None):
        assert hasattr(self, 'initial_data'), (
            'Cannot call `.is_valid()` as no `data=` keyword argument was '
            'passed when instantiating the serializer instance.'
        )

        if not hasattr(self, '_validated_data'):
            try:
                self._validated_data = self.run_validation(self.initial_data)
            except ValidationError as exc:
                self._validated_data = {}
                self._errors = exc.detail
                self._errors.update({'code':code, 'description':error_description if error_description is not None else CodeMessage.messages.get(code)})
            else:
                self._errors = {}
        if self._errors and raise_exception:
            raise ValidationError(self.errors)

        return not bool(self._errors)

def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

def validate_password_strength(value):
    """Validates that a password is as least 7 characters long and has at least
    1 digit and 1 letter.
    """
    min_length = 7

    if len(value) < min_length:
        raise ValidationError(_('Password must be at least {0} characters '
                                'long.').format(min_length))

    # check for digit
    if not any(char.isdigit() for char in value):
        raise ValidationError(_('Password must contain at least 1 digit.'))

    # check for letter
    if not any(char.isalpha() for char in value):
        raise ValidationError(_('Password must contain at least 1 letter.'))
