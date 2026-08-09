from tasks.models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tasks.forms import TaskForm
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/list.html'

class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = 'tasks/create.html'
    model = Task
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    pass

class TaskDeleteView(DeleteView):
    pass

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/detail.html'
