from django import forms
from .models import Project


class ProjectCreateForm(forms.ModelForm):
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