from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$',views.myweb_index,name='myweb_index'),
    url(r'^show$',views.show,name='show'),
    url(r'^show/(?P<tid>[0-9]+)$',views.show,name='show'),


    url(r'^content$',views.content,name='content'),
    url(r'^buycar$',views.buycar,name='buycar'),

    url(r'^myweb_add$',views.myweb_add,name='myweb_add'),
    url(r'^myweb_login$',views.myweb_login,name='myweb_login'),
    url(r'^myweb_dologin$', views.myweb_dologin, name="myweb_dologin"),
    url(r'^myweb_logout$', views.myweb_logout, name="myweb_logout"),
    url(r'^myweb_verify$', views.myweb_verify, name="myweb_verify"),
]
