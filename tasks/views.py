from tasks.models import Task, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tasks.forms import TaskForm, TaskFilterForm, CommentForm
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/list.html'

    def get_context_data(
            self, object_list=None, **kwargs
    ):
        context = super().get_context_data()
        context['filter_form'] = TaskFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        filter_form = TaskFilterForm(self.request.GET)

        if filter_form.is_valid():
            priority = filter_form.cleaned_data.get('priority')
            status = filter_form.cleaned_data.get('status')
            if priority:
                queryset = queryset.filter(priority=priority)
            if status:
                queryset = queryset.filter(status=status)

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

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        comments_qs = Comment.objects.filter(task=self.object)
        context['comments'] = comments_qs
        return context

class TaskDeleteView(DeleteView):
    pass

class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = 'tasks/comment_form.html'
    model = Comment

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.task_id = self.kwargs['pk']
        return super().form_valid(form)

    def success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.kwargs['pk']})
