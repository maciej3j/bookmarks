from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    #previous login url
    # path("login/", views.user_login, name="login"),
    # login /logout urls
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('', views.dashboard, name='dashboard'),
]