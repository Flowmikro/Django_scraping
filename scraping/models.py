from django.db import models
from django.utils import timezone


class Job(models.Model):
    url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return str(self.title)




