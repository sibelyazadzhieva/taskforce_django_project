from django.urls import path
from .views import worker_list, worker_create, worker_delete

urlpatterns = [
    path('', worker_list, name='worker-list'),
    path('add/', worker_create, name='worker-create'),
    path('<int:pk>/delete/', worker_delete, name='worker-delete'),
]