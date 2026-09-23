from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title