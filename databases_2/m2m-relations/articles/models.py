
from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField('Tag', through='ArticleTag', related_name='articles')

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=32, verbose_name='метка')


    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']

    def __str__(self):
        return self.title

class ArticleTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False, verbose_name='основная категория?')

    class Meta:
        verbose_name = 'тематика статьи'
        verbose_name_plural = 'тематики статьи'
        ordering = ['-is_main', '-tag']