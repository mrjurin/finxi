from django.conf.urls import url

from accounts.views import AccountsLoginView, AccountsLogoutView, RegisterView

urlpatterns = [
    url(r'^login/$', AccountsLoginView.as_view(), name='login'),
    url(r'^logout/$', AccountsLogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
]
