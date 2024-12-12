from django.urls import path
from . import views

urlpatterns = [
    path("",views.LogIn, name="LogIn"),
    path("Register",views.Register, name="Register"),
    path("LogOut",views.LogOut, name="LogOut"),
]