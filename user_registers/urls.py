from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('user_register', views.user_register, name= 'user_register'),
    path('login', views.login, name= 'login'),
    path('logout', views.logout, name= 'logout'),
    
]
