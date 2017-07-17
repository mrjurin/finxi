from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

User = get_user_model()


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    model = User
    success_url = reverse_lazy('index')


class AccountsLoginView(LoginView):
    template_name = 'accounts/login.html'


class AccountsLogoutView(LogoutView):
    template_name = 'accounts/login.html'
    next_page = '/'
