from django.urls import path
from .views import Userview,Loginview

 
urlpatterns = [
    path('api/', Userview.as_view()),
    path('api/<int:id>/', Userview.as_view()),
    path('login', Loginview.as_view())
]
