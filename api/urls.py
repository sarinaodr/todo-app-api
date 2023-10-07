from django.urls import path

from .views import ApiOverview , TaskListApi , TaskDetailApi , TaskCreateApi , TaskUpdateApi , TaskDeleteApi


urlpatterns = [
    path('' , ApiOverview , name='api-overview'),
    path('task-list' , TaskListApi , name='task-list'),
    path('task-detail/<int:pk>/' , TaskDetailApi , name='task-detail'),
    path('task-create/' , TaskCreateApi , name='task-create'),
    
    path('task-update/' , TaskUpdateApi , name='task-update'),
    path('task-delete/<int:pk>/' , TaskDeleteApi , name='task-delete'),
    
]
