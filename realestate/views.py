from django.views.generic import DetailView

from catalog.models import RealEstate


class ShowRealEstateView(DetailView):
    pk_url_kwarg = 'real_estate_id'
    model = RealEstate
    context_object_name = 'real_estate'
    template_name = 'realestate/show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recommendations'] = self.get_recommendations(context['real_estate'])
        return context

    def get_recommendations(self, real_estate):
        city_slug = real_estate.address.city.slug
        recommendations = RealEstate.objects.filter(address__city__slug=city_slug).exclude(pk=real_estate.pk)[:5]

        if len(recommendations):
            return recommendations

        state = real_estate.address.city.state
        return RealEstate.objects.filter(address__city__state=state).exclude(pk=real_estate.pk)[:5]
