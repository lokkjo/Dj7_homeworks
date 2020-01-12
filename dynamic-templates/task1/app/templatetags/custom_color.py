from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='custom_color')
@stringfilter
def custom_color(data):
    try:
        if float(data) < 0:
            color = 'DarkSeaGreen'
        elif float(data) < 1.0:
            color = 'white'
        elif float(data) < 2.0:
            color = 'Coral'
        elif float(data) < 5.0:
            color = 'OrangeRed'
        else:
            color = 'Red'
    except ValueError:
        color = 'white'
    return color