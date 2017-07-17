from django.conf.urls import url
from catalog.views import RealEstateBuyListView, RealEstateRentListView

urlpatterns = [
    url(r'^comprar/(?P<state>[\w]+)/(?P<slug>[\w-]+)/$',
        RealEstateBuyListView.as_view(),
        name='list_real_state_buy_param'
        ),

    url(r'^comprar/$',
        RealEstateBuyListView.as_view(),
        name='list_real_state_buy'
        ),

    url(r'^alugar/(?P<state>[\w]+)/(?P<slug>[\w-]+)/$',
        RealEstateRentListView.as_view(),
        name='list_real_state_rent_param'
        ),

    url(r'^alugar/$', RealEstateRentListView.as_view(), name='list_real_state_rent'), ]
