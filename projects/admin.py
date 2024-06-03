from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe

from .models import Skill, Project, Category


class NameSearch(admin.ModelAdmin):
    "Класс для получения кол-ва использований и добавления поля name"

    list_display = ('name',)
    search_fields = ('name',)

    @admin.display(
        description='Добавлено раз',
    )
    def get_uses(self, obj):
        """Получение количества добавлений в пет-проект."""
        return obj.projects.count()


@admin.register(Project)
class ProjectAdmin(NameSearch):
    "Настройка отображения модели project"

    list_display = NameSearch.list_display + (
        'pub_date', 'category', 'get_skills',
    )
    list_filter = ('category',)

    def image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} width="80" height="60">'
        )

    @admin.display(
        description='Навыки',
    )
    def get_skills(self, obj):
        result = ''
        for i in obj.skills.all():
            result += (f'{i.name}, ')
        return result[:-2]


@admin.register(Skill)
class SkillAdmin(NameSearch):
    "Настройка отображения модели skill"

    list_display = NameSearch.list_display + ('get_uses',)


@admin.register(Category)
class CategoryAdmin(NameSearch):
    "Настройка отображения модели Category"

    list_display = NameSearch.list_display + ('slug', 'get_uses',)


admin.site.unregister(Group)
