from django.urls import path

from core.views import CustomLoginView, UserRegistrationView

app_name = "core"

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
]
