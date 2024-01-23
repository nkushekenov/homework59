from django.db import models
from django.urls import reverse

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title