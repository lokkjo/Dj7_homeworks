from django.urls import register_converter

from .path_converters import DateUrlConverter

register_converter(DateUrlConverter, 'date')