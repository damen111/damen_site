from django.db import models

class Phase1(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='movies/', blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
    def __str__(self):
        return self.title

class Phase2(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='movies/', blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
    def __str__(self):
        return self.title

class Phase3(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='movies/', blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
    def __str__(self):
        return self.title

class Phase4(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='movies/', blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
    def __str__(self):
        return self.title

class Phase5(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='movies/', blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
    def __str__(self):
        return self.title

class Phase6(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='movies/', blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
    def __str__(self):
        return self.title