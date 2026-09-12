from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from account.views import dashboard

# from account import views

urlpatterns = [
    # path("login/", views.user_login, name="login")
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", dashboard, name="dashboard"),
]
