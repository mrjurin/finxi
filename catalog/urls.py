from django.conf.urls import url
from catalog.views import RealEstateBuyListView, RealEstateRentListView

urlpatterns = [
    url(r'^buy/(?P<state>[\w]+)/(?P<slug>[\w-]+)/$',
        RealEstateBuyListView.as_view(),
        name='list_real_state_buy_param'
        ),

    url(r'^buy/$',
        RealEstateBuyListView.as_view(),
        name='list_real_state_buy'
        ),

    url(r'^rent/(?P<state>[\w]+)/(?P<slug>[\w-]+)/$',
        RealEstateRentListView.as_view(),
        name='list_real_state_rent_param'
        ),

    url(r'^rent/$', RealEstateRentListView.as_view(), name='list_real_state_rent'), ]
