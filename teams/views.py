from django.shortcuts import render, redirect, get_object_or_404
from .models import Worker
from django import forms
from django.contrib import messages

def worker_list(request):
    workers = Worker.objects.all()
    return render(request, 'teams/worker_list.html', {'workers': workers})


def worker_create(request):
    class WorkerForm(forms.ModelForm):
        class Meta:
            model = Worker
            fields = '__all__'
            widgets = {
                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'role': forms.TextInput(attrs={'class': 'form-control'}),
            }

    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('worker-list')
    else:
        form = WorkerForm()

    return render(request, 'teams/worker_form.html', {'form': form})


def worker_delete(request, pk):
    worker = get_object_or_404(Worker, pk=pk)

    if request.method == 'POST':
        problematic_projects = []

        for project in worker.projects.all():
            if project.team_members.count() == 1:
                problematic_projects.append(project.name)

        if problematic_projects:
            projects_str = ", ".join(problematic_projects)
            messages.error(
                request,
                f"Cannot remove {worker.first_name}. They are the ONLY member in: {projects_str}. Please assign someone else to these projects first."
            )
            return redirect('worker-delete', pk=worker.pk)

        worker.delete()
        return redirect('worker-list')

    return render(request, 'teams/worker_confirm_delete.html', {'worker': worker})