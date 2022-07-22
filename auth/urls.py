from django.urls import path
from auth import views

urlpatterns=[
    path('login/',views.login.as_view() , name='auth_login'),
    path('logout/',views.logout.as_view() , name='auth_logout'),
]