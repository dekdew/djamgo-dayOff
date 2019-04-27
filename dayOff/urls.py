from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('register/', views.my_register, name='register'),
    path('new/', views.newDayOff, name='newDayOff'),
]
