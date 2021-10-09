from django.urls import path
from .views import get_all_tasks, get_todos, complete_task

urlpatterns = [
    path('tasks/', get_all_tasks),
    path('todo/', get_todos),
    path('done/<int:pk>', complete_task)
]