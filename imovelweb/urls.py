from django.conf.urls import url, include
from django.contrib import admin
from core.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='index'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^realestate/', include('realestate.urls')),
    url(r'^admin/', admin.site.urls),
]
