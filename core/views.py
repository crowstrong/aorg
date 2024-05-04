from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, View

from core.forms import UserRegistrationForm


class AmodiusHomePage(TemplateView):
    template_name = "index.html"


class Error404(TemplateView):
    template_name = "errors/404.html"


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = "registration/register.html"  # Создайте шаблон для страницы регистрации
    success_url = reverse_lazy("login")  # Перенаправление после успешной регистрации


class CustomLoginView(LoginView):
    template_name = "registration/login.html"  # Создайте шаблон для страницы входа в систему
    success_url = reverse_lazy("index")  # Перенаправление после успешного входа


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))  # Перенаправляем пользователя на страницу входа после выхода
