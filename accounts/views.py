from django.shortcuts import resolve_url as r, render
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.models import RealEstate
from realestate.forms import RealEstateCreationForm, AddressForm
from .forms import UserAdminCreationForm

User = get_user_model()


class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')


class AccountsIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'


class AccountsLoginView(LoginView):
    template_name = 'accounts/login.html'


class AccountsLogoutView(LogoutView):
    template_name = 'accounts/login.html'


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user


class AddRealEstateView(LoginRequiredMixin, CreateView):
    model = RealEstate
    template_name = 'accounts/add_real_estate.html'
    form_class = RealEstateCreationForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        address_form = AddressForm(request.POST)

        if not address_form.is_valid():
            return render(request, 'accounts/add_real_estate.html', {'form': address_form})

        address = address_form.save(commit=False)
        real_estate_form = RealEstateCreationForm(request.POST)
        real_estate_form.fields['address'] = address
        # real_estate_form.fields['seller'] = User.objects.get(id=7)

        if not real_estate_form.is_valid():
            return render(request, 'accounts/add_real_estate.html', {'form': real_estate_form})

        # real_estate_form.fields.seller =
        real_estate_form.save()


        # address = address_form.save()

        # real_estate_form.save()
        # if form.is_valid():
        #     data = {
        #         'real_state': form.data
        #     }
        #
        #     data['real_estate']['address']['number'] = form.number
        #     data['real_estate']['address']['neighborhood'] = form.neighborhood
        #     data['real_estate']['address']['postal_code'] = form.postal_code
        #     data['real_estate']['address']['city'] = form.city
        #
        #     real_estate = RealEstate(data)
        #     real_estate.save()
        #     # property.owner = request.user
        #     # property.image = request.FILES['image']
        #     # property.save()
        #     return redirect(r('realestate:show_real_estate', real_estate_id=real_estate.id))
        return super().post(request, *args, **kwargs)
