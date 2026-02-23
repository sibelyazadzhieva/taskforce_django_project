from django.urls import path
from .views import project_list, project_create, project_details, project_edit, project_delete, task_create, task_edit, task_delete

urlpatterns = [
    path('', project_list, name='project-list'),
    path('create/', project_create, name='project-create'),
    path('<int:pk>/', project_details, name='project-details'),
    path('<int:pk>/edit/', project_edit, name='project-edit'),
    path('<int:pk>/delete/', project_delete, name='project-delete'),
    path('<int:project_pk>/tasks/add/', task_create, name='task-create'),
    path('tasks/<int:pk>/edit/', task_edit, name='task-edit'),
    path('tasks/<int:pk>/delete/', task_delete, name='task-delete'),
]