from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'элемент'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class ThematicTag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)
    article_tag = models.ManyToManyField(Article, through='TagsRelation')

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'тег'

    def __str__(self):
        return self.name


class TagsRelation(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(ThematicTag, on_delete=models.CASCADE, related_name='scopes', verbose_name='имя тега')
    is_main = models.BooleanField(verbose_name='основной')

    class Meta:
        verbose_name_plural = 'Выбор тега'
        ordering = ['-is_main']
        unique_together = ("article", "tag",)

