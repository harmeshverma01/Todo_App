from tokenize import Name
from django.db import models

# Create your models here.

class User(models.Model):
    ROLE_CHOICES = (
        ("admin", "admin"),
        ("Manager", "Manager"),
        ("User", "User")
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    role = models.CharField(choices=ROLE_CHOICES, max_length=15, null=True)
    date = models.DateTimeField(null=True)
    
    def __str__(self) -> str:
        return(self.name)