from django import template
from django.template.defaultfilters import stringfilter

import json


# Если инфляция за месяц была отрицательной (дефляция), то
# ячейка должна быть закрашена в зеленый. Если значение инфляции
# превысило 1%, то в красный. Должна быть реализована визуальная
# градация красного: от 1% до 2%, от 2% до 5%, от 5% и более
# (3 оттенка красного, визуально они должны быть различимы).



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
    print('data', data, color)
    return color