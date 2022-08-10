from django.urls import path, include
from .views import TaskView


urlpatterns = [
    path('task/', TaskView.as_view()),
]
