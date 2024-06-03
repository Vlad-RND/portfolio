from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path(
        '',
        views.IndexListView.as_view(),
        name='index'
    ),
    path(
        'projects/<int:pk>/',
        views.ProjectDitailView.as_view(),
        name='project_detail'
    ),
    path(
        'categories/<slug:slug>/',
        views.CategoryListView.as_view(),
        name='category'
    ),
    path(
        'skills/<slug:slug>/',
        views.SkillListView.as_view(),
        name='skill'
    ),
]
