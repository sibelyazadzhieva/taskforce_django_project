from django import forms
from .models import Project, Task, Worker
from datetime import date

class ProjectCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deadline'].widget.attrs['min'] = date.today().isoformat()

    class Meta:
        model = Project
        fields = ['name', 'description', 'deadline', 'team_members']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'team_members': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Project Title',
            'team_members': 'Assign Team Members',
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        if deadline and deadline < date.today():
            raise forms.ValidationError("The deadline cannot be in the past!")
        return deadline

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['title'].disabled = True
            self.fields['title'].help_text = "Task title cannot be changed once created."

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'assignee']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'assignee': forms.Select(attrs={'class': 'form-select'}),
        }
class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'

class TaskSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by title...',
            'class': 'form-control',
            'style': 'border-radius: 8px;'
        })
    )