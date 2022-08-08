from django.urls import path
from .views import TasKView, Userview,Loginview, UserDetailsView

 
urlpatterns = [
    path('api-users/', Userview.as_view()),
    path('login', Loginview.as_view()),
    path('UserDetails/<uuid:id>', UserDetailsView.as_view()),
    path('task/', TasKView.as_view()),
]
