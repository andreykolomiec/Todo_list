from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'task_list/task_list.html'


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'task_list/task_detail.html'


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task_list:task_list")
    template_name = "task_list/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task_list:task_list")
    template_name = "task_list/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_list:task_list")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = "task_list/tags.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task_list:tags")
    template_name = "task_list/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task_list:tags")
    template_name = "task_list/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task_list:tags")
    template_name = "task_list/tag_delete.html"