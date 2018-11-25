from django.urls import path
from rob_s5 import views

urlpatterns = [
    path("", views.home, name="home"),
    path('login',views.login,name="login"),
    path('logpage',views.logpage,name="logpage"),
    path("home",views.home,name="home"),
]