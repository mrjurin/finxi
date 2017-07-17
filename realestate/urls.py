from django.conf.urls import url
from realestate.views import ShowRealEstateView

urlpatterns = [
    url(r'^imovel/(?P<real_estate_id>[\w\d-]+)/$', ShowRealEstateView.as_view(), name='show_real_estate'),
]
