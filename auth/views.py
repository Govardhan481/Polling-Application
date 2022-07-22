from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,
    LogoutView
    )

# Create your views here.


class login(LoginView):
    template_name='auth/login.html'
    redirect_authenticated_user = True


class logout(LogoutView):
    template_name='auth/logout.html'
