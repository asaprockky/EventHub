from django.urls import path
from .views import SignupView, CustomLogin, ProfielView
from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    path("login/", CustomLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("profile/", ProfielView.as_view(), name="profile"),
]
