from django.views.generic import TemplateView


class RealEstateListView(TemplateView):
    template_name = 'catalog/real_estate_list.html'
