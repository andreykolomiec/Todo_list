from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_task = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)

    class Meta:
        ordering = ["is_done", "-created_task"]

    def __str__(self):
        tags_str = ", ".join(self.tags.values_list("name", flat=True))
        return (
            f"{self.content},"
            f"{'Done' if self.is_done else 'Not Done}'},"
            f"Created: {self.created_task},"
            f" {self.deadline}"
            f"Tags: {tags_str}"
        )
