from django.conf.urls import url
from accounts.views import AccountsLoginView, AccountsLogoutView, RegisterView, AccountsIndexView, UpdateUserView

urlpatterns = [
    url(r'^minhaconta/$', AccountsIndexView.as_view(), name='index'),
    url(r'^minhaconta/editar/$', UpdateUserView.as_view(), name='update_user'),
    url(r'^login/$', AccountsLoginView.as_view(), name='login'),
    url(r'^logout/$', AccountsLogoutView.as_view(), name='logout'),
    url(r'^registrar/$', RegisterView.as_view(), name='register'),
]
