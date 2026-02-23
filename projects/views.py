from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectCreateForm, TaskForm, Task

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

def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_details.html', {'project': project})


def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project-details', pk=pk)
    else:
        form = ProjectCreateForm(instance=project)

    return render(request, 'projects/project_edit.html', {'form': form, 'project': project})


def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project-list')

    return render(request, 'projects/project_confirm_delete.html', {'project': project})

def task_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project-details', pk=project.pk)
    else:
        form = TaskForm()
    return render(request, 'projects/task_form.html', {'form': form, 'project': project})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project = task.project

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project-details', pk=project.pk)
    else:
        form = TaskForm(instance=task)

    return render(request, 'projects/task_form.html', {
        'form': form,
        'task': task,
        'project': project,
        'edit_mode': True
    })
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project_pk = task.project.pk
    if request.method == 'POST':
        task.delete()
        return redirect('project-details', pk=project_pk)
    return render(request, 'projects/task_confirm_delete.html', {'task': task})