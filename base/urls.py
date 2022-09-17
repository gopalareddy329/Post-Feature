from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name="home"),
    path('logout/',views.logoutuser,name="logoutuser"),
    path('posts/',views.Post_User,name="posts"),
    path('add/',views.addpost,name="add"),
]