from django.contrib import admin
from task_list.models import Tag, Task

admin.site.register(Tag)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "created_task", "deadline", "is_done",]
    list_filter = ["is_done",]
    search_fields = ["tags__name"]