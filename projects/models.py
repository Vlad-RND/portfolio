from django.db import models

from .constants import NAME_LENGTH, SHORT_NAME_LEN


class NameModel(models.Model):
    """Абстрактная модель для добавления поля name."""

    name = models.CharField(
        'Название',
        max_length=NAME_LENGTH,
        unique=True,
    )

    class Meta:
        abstract = True
        ordering = ('name',)


class SlugNameModel(NameModel):
    """Абстрактная модель для добавления поля name и slug."""

    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text='Идентификатор страницы для URL;'
        ' разрешены символы латиницы, цифры, дефис и подчёркивание.',
    )

    class Meta:
        abstract = True


class Category(SlugNameModel):
    """Модель категории"""

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        default_related_name = 'categories'

    def __str__(self):
        return self.name[:SHORT_NAME_LEN]


class Skill(SlugNameModel):
    """Модель навыка"""

    class Meta:
        verbose_name = 'навык'
        verbose_name_plural = 'Навыки'
        default_related_name = 'skills'

    def __str__(self):
        return self.name[:SHORT_NAME_LEN]


class Project(NameModel):
    """Модель пет-проекта."""

    skills = models.ManyToManyField(
        Skill,
        verbose_name='Навыки',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
    )
    description = models.TextField('Описание')
    url = models.URLField('Ссылка', unique=True)
    image = models.ImageField(
        'Изображение',
        upload_to='media/',
    )
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Пет-проект'
        verbose_name_plural = 'Пет-проекты'
        ordering = ('-pub_date', 'name',)
        default_related_name = 'projects'

    def __str__(self):
        return self.name[:SHORT_NAME_LEN]
