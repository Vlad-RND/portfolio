from http import HTTPStatus

from django.shortcuts import render
from django.views.generic import TemplateView

from projects.models import Project, Skill


class InfoPage(TemplateView):
    """Подготовка данных для страницы 'О себе'."""

    template_name = 'pages/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects_count'] = Project.objects.count()
        context['skills'] = Skill.objects.all()
        context['resume'] = '/media/media/resume/Резюме.pdf'
        return context


def page_not_found(request, exception):
    """Обработка страницы с ошибкой 404."""
    return render(request, 'pages/404.html', status=HTTPStatus.NOT_FOUND)


def server_error(request, *args, **argv):
    """Обработка страницы с ошибкой 500."""
    return render(
        request,
        'pages/500.html',
        status=HTTPStatus.INTERNAL_SERVER_ERROR
    )
