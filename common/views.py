from django.shortcuts import render
from projects.models import Project, Task
from teams.models import Worker

def index(request):
    context = {
        'total_projects': Project.objects.count(),
        'total_tasks': Task.objects.count(),
        'total_workers': Worker.objects.count(),
        'recent_tasks': Task.objects.order_by('-id')[:3],
    }
    return render(request, 'common/index.html', context)