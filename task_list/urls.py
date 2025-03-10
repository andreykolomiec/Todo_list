from django.urls import path

from task_list.views import (
    TaskListView,
    TagListView,
    TaskUpdateView,
    TaskDetailView,
    TaskCreateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("task_list/", TaskListView.as_view(), name="task_list"),
    path("task_list/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("task_list/create/", TaskCreateView.as_view(), name="task_create"),
    path("task_list/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("task_list/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tags_list/create/", TagCreateView.as_view(), name="tags_create"),
    path("tags_list/<int:pk>/update/", TagUpdateView.as_view(), name="tags_update"),
    path("tags_list/<int:pk>/delete/", TagDeleteView.as_view(), name="tags_delete"),
]

app_name = "task_list"