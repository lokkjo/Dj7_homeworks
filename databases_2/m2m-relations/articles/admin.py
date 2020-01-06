from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag


class TaggingInlineFormset(InlineModelAdmin):
    def clean(self):
        for form in self.forms:
            form.cleaned_data
            raise ValidationError('Тут всегда ошибка')
        return super().clean()

class TaggingInline(admin.TabularInline):
    model = Tag.tagged_article.through


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TaggingInline,]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [TaggingInline,]
    # exclude = ('tags',)