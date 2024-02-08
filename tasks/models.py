from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Update the 'updated_at' field before saving the object
        self.updated_at = timezone.now()
        super(Task, self).save(*args, **kwargs)