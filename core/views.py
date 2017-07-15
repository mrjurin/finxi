from django.views.generic import TemplateView

from catalog.models import City, RealEstate


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cities = City.objects.filter(capital=True)
        real_estates = RealEstate.objects.all()[:6]
        context['grouped_real_estates'] = self.to_groups(real_estates, 3)
        context['grouped_cities'] = self.to_groups(cities, 3)
        return context

    def to_groups(self, element_list, number):
        for i in range(0, len(element_list), number):
            yield element_list[i:i + number]
