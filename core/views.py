from django.views.generic import TemplateView

from catalog.models import City


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cities = City.objects.filter(capital=True)
        context['grouped_cities'] = self.to_groups(cities)
        return context

    def to_groups(self, cities):
        size = len(cities)
        if not size:
            return []

        hop = int(size / 3)
        return [
            cities[0:hop],
            cities[hop: size - hop],
            cities[hop + hop:]
        ]
