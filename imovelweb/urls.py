from django.conf.urls import url, include
from django.contrib import admin
from core.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='index'),
    url(r'^contas/', include('accounts.urls', namespace='accounts')),
    url(r'^imoveis/', include('catalog.urls', namespace='catalog')),
    url(r'^imovel/', include('realestate.urls', namespace='realestate')),
    url(r'^admin/', admin.site.urls),
]
