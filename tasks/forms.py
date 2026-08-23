from django import forms
from tasks.models import Task, Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date', 'priority']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),    
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }

class TaskFilterForm(forms.Form):
    priority = forms.ChoiceField(
        choices=[('', 'Всі')] + Task.PRIORITY_CHOICES,
        label='Пріоритет',
        required=False,
        widget = forms.Select(attrs={'class': 'form-control'}),
    )
    status = forms.ChoiceField(
        choices=[('', 'Всі')] + Task.STATUS_CHOICES,
        label='Статус',
        required=False,
        widget = forms.Select(attrs={'class': 'form-control'}),
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
