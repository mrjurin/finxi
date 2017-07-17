from django.conf.urls import url, include
from django.contrib import admin
from catalog.views import RealEstateBuyListView, RealEstateRentListView
from core.views import HomePageView
from realestate.views import ShowRealEstateView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='index'),
    url(r'^accounts/', include('accounts.urls')),

    url(r'^comprar/(?P<state>[\w]+)/(?P<slug>[\w-]+)/$', RealEstateBuyListView.as_view(),
        name='list_real_state_buy_param'),
    url(r'^comprar/$', RealEstateBuyListView.as_view(), name='list_real_state_buy'),

    url(r'^alugar/(?P<state>[\w]+)/(?P<slug>[\w-]+)/$', RealEstateRentListView.as_view(),
        name='list_real_state_rent_param'),
    url(r'^alugar/$', RealEstateRentListView.as_view(), name='list_real_state_rent'),

    url(r'^imovel/(?P<real_estate_id>[\w\d-]+)/$', ShowRealEstateView.as_view(), name='show_real_estate'),
    url(r'^admin/', admin.site.urls),
]
