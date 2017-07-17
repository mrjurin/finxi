from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserAdminCreationForm

User = get_user_model()


class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')


class AccountsLoginView(LoginView):
    template_name = 'accounts/login.html'


class AccountsLogoutView(LogoutView):
    template_name = 'accounts/login.html'
    next_page = '/'
