from django.urls import path
from .views import Userview,Loginview, UserDetailsView

 
urlpatterns = [
    path('api-users/', Userview.as_view()),
    path('api/<int:id>/', Userview.as_view()),
    path('login', Loginview.as_view()),
    path('UserDetails', UserDetailsView.as_view())
]
