from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.userRegister, name="user.register"),
    path('login/', views.userlogin, name="user.login"),
    path('logout/',views.userLogout,name='user.logout'),
]