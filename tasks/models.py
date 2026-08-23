from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', "До роботи"),
        ('in_progress', "В процесі"),
        ('done', "Завершено"),
    ]
    
    PRIORITY_CHOICES = [
        ('low', "Низький"),
        ('medium', "Середній"),
        ('high', "Високий"),
        ('very_high', "Дуже високий"),
    ]
    
    
    title = models.CharField(max_length=150, verbose_name='Назва')
    description = models.TextField(verbose_name='Опис')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='todo', verbose_name='Статус')
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES, verbose_name='Пріоритет')
    due_date = models.DateField(blank=True, null=True, verbose_name='Дата виконання')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', verbose_name='Власний')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачі'
        ordering = ['-created_at']

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments', verbose_name='Задача')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='a_comments', verbose_name='Автор')
    content = models.TextField(verbose_name='Текст')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.last_name} {self.author.first_name} - {self.task.title}'


    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ['-created_at']
   