from django.urls import path
from .views import  Userview,Loginview, UserDetailsView, ManagerView, AssignUserView

 
urlpatterns = [
    path('api-users/', Userview.as_view()),
    path('login', Loginview.as_view()),
    path('UserDetails/<uuid:id>', UserDetailsView.as_view()),
    path('Manager', ManagerView.as_view()),
    path('AssignView', AssignUserView.as_view()),

]
