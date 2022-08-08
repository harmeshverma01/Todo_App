from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager
import uuid
from app import manager


# Create your models here.

class User(AbstractBaseUser):
    ROLE_CHOICES = (
        ("admin", "admin"),
        ("Manager", "Manager"),
        ("User", "User")
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.CharField(choices=ROLE_CHOICES, max_length=15)
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    objects = UserManager()
    

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['name', 'password']
    
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    
    def __str__(self) -> str:
        return(self.name)
    
class Assign(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="User", null=True)
    manager = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)   
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=50, null=True)
    completed = models.BooleanField(default=False, blank=True)
    objects = models.Manager()
    
    def __str__(self) -> str:
        return self.title
                