from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loginUser, name="loginUser"),
    path('logout/', views.logoutUser, name="logoutUser"),
]
