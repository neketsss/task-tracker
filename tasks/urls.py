from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('detail/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task_delete'),
]