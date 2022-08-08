from django.contrib import admin
from .models import User

app_name = 'app'

# Register your models here.
admin.site.register(User)