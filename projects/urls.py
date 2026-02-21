from django.urls import path
from .views import project_list, project_create

urlpatterns = [
    path('', project_list, name='project-list'),
    path('create/', project_create, name='project-create'),
]