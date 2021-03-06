from django.views.generic import ListView

from catalog.models import RealEstate, SELL, RENT


class RealEstateListView(ListView):
    template_name = 'catalog/real_estate_list.html'
    paginate_by = 10


class RealEstateBuyListView(RealEstateListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Comprar'
        return context

    def get_queryset(self):
        city_slug = self.kwargs.get('slug', None)
        state_abbrev = self.kwargs.get('state', None)

        objects = RealEstate.objects.filter(sold=False).exclude(transaction_type=RENT)
        if city_slug:
            objects = objects.filter(address__city__slug=city_slug)

        if state_abbrev:
            objects = objects.filter(address__city__state__abbreviation__contains=state_abbrev)
        return objects


class RealEstateRentListView(RealEstateListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Alugar'
        return context

    def get_queryset(self):
        city_slug = self.kwargs.get('slug', None)
        state_abbrev = self.kwargs.get('state', None)

        objects = RealEstate.objects.filter(sold=False).exclude(transaction_type=SELL)
        if city_slug:
            objects = objects.filter(address__city__slug=city_slug)

        if state_abbrev:
            objects = objects.filter(address__city__state__abbreviation__contains=state_abbrev)
        return objects
