from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bug(models.Model):
    STATUS_CHOICES = (
        ('todo', 'To do'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    )
    name = models.CharField(max_length=254)
    description = models.TextField()
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default="todo")
    upvotes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, default= 1)
    
    def __str__(self):
        return self.name