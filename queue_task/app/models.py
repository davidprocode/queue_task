from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=64, blank=False)
    description = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
