import logging
from . import views
from django.urls import path

urlpatterns = [
    path("login",views.login_register_request,name = "login_register"),
    path("logout",views.logout_request,name="logout"),
]
