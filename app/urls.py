from django.urls import path
from .views import  Userview,Loginview, UserDetailsView, ManagerView, AssignUserView
from . import views

 
urlpatterns = [
    path('api-users/', Userview.as_view()),
    path('login', Loginview.as_view()),
    path('UserDetails/<uuid:id>', UserDetailsView.as_view()),
    path('Manager', ManagerView.as_view()),
    path('Admin-Assign', AssignUserView.as_view()),
    path('list-user', views.getuser, name='getuser')
]
