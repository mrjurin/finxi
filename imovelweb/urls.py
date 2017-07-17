from django.conf.urls import url, include
from django.contrib import admin
from core.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='index'),
    url(r'^contas/', include('accounts.urls')),
    url(r'^imoveis/', include('catalog.urls')),
    url(r'^imovel/', include('realestate.urls')),
    url(r'^admin/', admin.site.urls),
]
