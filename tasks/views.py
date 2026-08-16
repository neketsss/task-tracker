from tasks.models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tasks.forms import TaskForm, TaskFilterForm
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/list.html'

    def get_context_data(
            self, object_list=None, **kwargs
    ):
        context = super().get_context_data()
        context['filter_form'] = TaskFilterForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        filter_form = TaskFilterForm(self.request.GET)

        if filter_form.is_valid():
            queryset = queryset.filter(**filter_form.cleaned_data)

        return queryset

class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = 'tasks/form.html'
    model = Task
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    form_class = TaskForm
    template_name = 'tasks/form.html'
    model = Task
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    pass

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/detail.html'
