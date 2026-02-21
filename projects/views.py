from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectCreateForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


def project_create(request):
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project-list')
    else:
        form = ProjectCreateForm()

    return render(request, 'projects/project_create.html', {'form': form})