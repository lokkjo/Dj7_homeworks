from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    image = models.FileField(max_length=32)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    # slug_string = slugify(name) # тут слагифицируем name
    slug = models.CharField(max_length=32)
    # slug = slug_string

    def __str__(self):
        return f'{self.name}'
