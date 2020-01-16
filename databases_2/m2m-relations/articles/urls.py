from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from articles.views import articles_list

urlpatterns = [
    path('', articles_list, name='articles'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
