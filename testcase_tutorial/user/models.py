from django.db import models

# Create your models here.
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    bio = models.TextField()

    def __str__(self):
        return self.username
