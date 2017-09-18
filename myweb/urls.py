from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.myweb_index,name='myweb_index'),
    url(r'^show$',views.show,name='show'),
    url(r'^show/(?P<tid>[0-9]+)$',views.show,name='show'),


    url(r'^content/(?P<tid>[0-9]+)$',views.content,name='content'),
    url(r'^contentbuy/(?P<tid>[0-9]+)$',views.contentbuy,name='contentbuy'),
    url(r'^buycar$',views.buycar,name='buycar'),
    url(r'^buycardel/(?P<tid>[0-9]+)$',views.buycardel,name='buycardel'),
    url(r'^buycarclear$',views.buycarclear,name='buycarclear'),

    url(r'^selfcenter$',views.selfcenter,name='selfcenter'),
    url(r'^selfinformation$',views.selfinformation,name='selfinformation'),
    url(r'^selforder/(?P<pIndex>[0-9]+)$',views.selforder,name='selforder'),
    url(r'^selfdetail/(?P<oid>[0-9]+)$',views.selfdetail,name='selfdetail'),



    url(r'^myweb_add$',views.myweb_add,name='myweb_add'),
    url(r'^myweb_login$',views.myweb_login,name='myweb_login'),
    url(r'^myweb_dologin$', views.myweb_dologin, name="myweb_dologin"),
    url(r'^myweb_logout$', views.myweb_logout, name="myweb_logout"),
    url(r'^myweb_verify$', views.myweb_verify, name="myweb_verify"),

    url(r'^myweb_orderlist$', views.myweb_orderlist, name="myweb_orderlist"),
    url(r'^myweb_orderconfirm$', views.myweb_orderconfirm, name="myweb_orderconfirm"),

    url(r'^myweb_orderinsert$', views.myweb_orderinsert, name="myweb_orderinsert"),



]
