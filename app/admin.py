from django.contrib import admin
from .models import Assign, Task, User

app_name = 'app'

# Register your models here.
admin.site.register(User)
admin.site.register(Assign)
admin.site.register(Task)