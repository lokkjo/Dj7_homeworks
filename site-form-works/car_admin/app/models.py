from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='марка')
    model = models.CharField(max_length=50, verbose_name='модель')

    def __str__(self):
        return f'{self.brand} {self.model}'

    class Meta:
        ordering = ('-id',)
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


    def review_count(self):

        return Review.objects.filter(car=self).count()


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='машина')
    title = models.CharField(max_length=100, verbose_name='заголовок')
    text = models.TextField()

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return str(self.car) + ' ' + self.title

