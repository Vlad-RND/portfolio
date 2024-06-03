from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from .constants import PROJECTS_LIMIT
from .models import Category, Project, Skill


class ProjectPaginateTemplate(ListView):
    "Класс-родитель для добавления полей"

    model = Project
    template_name = 'projects/index.html'
    paginate_by = PROJECTS_LIMIT


class IndexListView(ProjectPaginateTemplate):
    "Отображение главной страницы"

    pass


class CategoryListView(ProjectPaginateTemplate):
    "Оторбражение страницы с фильтрацией по категории"

    def get_queryset(self):
        return get_object_or_404(
            Category, slug=self.kwargs['slug']
        ).projects.all()


class SkillListView(ProjectPaginateTemplate):
    "Оторбражение страницы с фильтрацией по умению"

    def get_queryset(self):
        return get_object_or_404(
            Skill, slug=self.kwargs['slug']
        ).projects.all()


class ProjectDitailView(DetailView):
    "Оторбражение страницы конкретного проекта"

    model = Project
    template_name = 'projects/detail.html'
