from django.shortcuts import render
from tasks.models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/list.html'

class TaskCreateView(CreateView):
    pass

class TaskUpdateView(UpdateView):
    pass

class TaskDeleteView(DeleteView):
    pass

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/detail.html'
