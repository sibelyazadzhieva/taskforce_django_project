from django.db import models
from teams.models import Worker
from django.core.exceptions import ValidationError


def validate_min_length(value):
    if len(value) < 10:
        raise ValidationError("Description must be at least 10 characters long!")

class Project(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(validators=[validate_min_length])
    deadline = models.DateField()

    team_members = models.ManyToManyField(Worker, related_name='projects')

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='todo'
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    assignee = models.ForeignKey(
        'teams.Worker',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks'
    )

    def __str__(self):
        return self.title

