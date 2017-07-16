from django.views.generic import ListView

from catalog.models import RealEstate, SELL, RENT


class RealEstateListView(ListView):
    template_name = 'catalog/real_estate_list.html'
    paginate_by = 10

    def get_queryset(self):
        return RealEstate.objects.filter(sold=False)


class RealEstateBuyListView(RealEstateListView):
    def get_queryset(self):
        return RealEstate.objects.filter(sold=False).exclude(transactionType=RENT)


class RealEstateRentListView(RealEstateListView):
    def get_queryset(self):
        return RealEstate.objects.filter(sold=False).exclude(transactionType=SELL)
