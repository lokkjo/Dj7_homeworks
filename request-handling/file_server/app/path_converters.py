from datetime import date, datetime

from django.urls import register_converter

class DateUrlConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'

    def to_python(self, value: str) -> date:
        return datetime.strptime(value, self.format).date()

    def to_url(self, value: date) -> str:
        return value.strftime(self.format)


# register_converter(DateUrlConverter, 'date')