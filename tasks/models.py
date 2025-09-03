from django.db import models
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
