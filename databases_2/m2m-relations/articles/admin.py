
from django.contrib import admin

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_counter = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            data = form.cleaned_data
            if data.get('is_main'):
                is_main_counter +=1
            if is_main_counter == 0:
                raise ValidationError('Укажите основной раздел')
            elif is_main_counter > 1:
                raise ValidationError('Основным может быть только один раздел')
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ArticleTagInline(admin.TabularInline):

    model = ArticleTag
    formset = ArticleTagInlineFormset

    class Meta:
        verbose_name = 'категория'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInline]
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

