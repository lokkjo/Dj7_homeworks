
from django.views.generic import ListView
from django.shortcuts import render

from pprint import pprint

from articles.models import Article, Tag, ArticleTag

def articles_list(request):
    template = 'articles/news.html'
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    ordering = '-published_at'

    articles = Article.objects.all().prefetch_related('tags')\
        .order_by(ordering)

    # Доступ к полю is_main
    # for article in articles:
    #     tags = article.tags.all().values_list(
    #     'articletag__tag__title','articletag__is_main'
    #     ).order_by('articletag')

    context = {'articles': articles}

    return render(request, template, context)