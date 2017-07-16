"""aluguelimoveis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from catalog.views import RealEstateBuyListView, RealEstateRentListView
from core.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^comprar/(?P<state>[\w]+)/(?P<slug>[\w-]+)/$', RealEstateBuyListView.as_view(), name='list_real_state_buy_param'),
    url(r'^comprar/$', RealEstateBuyListView.as_view(), name='list_real_state_buy'),

    url(r'^alugar/(?P<state>[\w]+)/(?P<slug>[\w-]+)/$', RealEstateRentListView.as_view(), name='list_real_state_rent_param'),
    url(r'^alugar/$', RealEstateRentListView.as_view(), name='list_real_state_rent'),
    url(r'^admin/', admin.site.urls),
]

# url(r'^palestrantes/(?P<slug>[\w-]+)/$', speaker_detail, name='speaker_detail'),
# /imoveis/comprar/sp/sao-paulo
# /imoveis/alugar/rs/porto-alegre