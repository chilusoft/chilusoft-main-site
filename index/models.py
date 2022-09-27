from django.db import models

from django.contrib.auth.models import AbstractUser
from djrichtextfield.models import RichTextField

# Create your models here.

class User(AbstractUser):
    ACCESS_LEVEL_CHOICE = (
        (1, 'Super User'),
        (2, 'Admin'),
        (3, 'User'),
    )
    access_level = models.IntegerField(default=3, choices=ACCESS_LEVEL_CHOICE)

    def __str__(self):
        return self.username

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField()
    hyperlink = models.URLField()
    image = models.ImageField(upload_to='project_category', default='project_category/default.png', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name - self.category.name

