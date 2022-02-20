from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ThematicTag, TagsRelation


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        err = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # if form.cleaned_data['tag_is_main']:
            if form.cleaned_data.get('is_main'):
                err += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if not err:
            raise ValidationError('Нет основного тега')
        elif err > 1:
            raise ValidationError('Основной тег должен быть один')
        return super().clean()  # вызываем базовый код переопределяемого метода


class TagsRelationInLine(admin.TabularInline):
    model = TagsRelation
    extra = 0
    formset = RelationshipInlineFormset
    verbose_name = "тег"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at']
    inlines = [TagsRelationInLine]


@admin.register(ThematicTag)
class ThematicTagAdmin(admin.ModelAdmin):
    list_display = ['name']
