from django.conf.urls import url

from . import views
from . import typeviews


urlpatterns = [
    url(r'^$', views.index,name='index'),

    # 后台用户管理
    url(r'^users/(?P<pIndex>[0-9])$', views.usersindex, name="usersindex"),
    url(r'^usersadd$', views.usersadd, name="usersadd"),
    url(r'^usersinsert$', views.usersinsert, name="usersinsert"),
    url(r'^usersdel/(?P<uid>[0-9]+)$', views.usersdel, name="usersdel"),
    url(r'^usersedit/(?P<uid>[0-9]+)$', views.usersedit, name="usersedit"),
    url(r'^usersupdate$', views.usersupdate, name="usersupdate"),
    #登录
    url(r'^login$', views.login, name="login"),
    url(r'^dologin$', views.dologin, name="dologin"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^verify$', views.verify, name="verify"),
 
    #商品类型
    url(r'^type/(?P<pIndex>[0-9])$', typeviews.typeindex, name="typeindex"),
    url(r'^typeadd/(?P<id1>[0-9]+)$', typeviews.typeadd, name="typeadd"),
    url(r'^typeinsert$', typeviews.typeinsert, name="typeinsert"),
    url(r'^typedel/(?P<uid>[0-9]+)$', typeviews.typedel, name="typedel"),
    url(r'^typeedit/(?P<uid>[0-9]+)$', typeviews.typeedit, name="typeedit"),
    url(r'^typeupdate$', typeviews.typeupdate, name="typeupdate"),


    #商品信息
    url(r'^goods/(?P<pIndex>[0-9])$', typeviews.goodsindex, name="goodsindex"),
    url(r'^goodsadd/(?P<gid>[0-9]+)$', typeviews.goodsadd, name="goodsadd"),
    url(r'^goodsinsert$', typeviews.goodsinsert, name="goodsinsert"),
    url(r'^goodsdel/(?P<gid>[0-9]+)$', typeviews.goodsdel, name="goodsdel"),
    url(r'^goodsedit/(?P<gid>[0-9]+)$', typeviews.goodsedit, name="goodsedit"),
    url(r'^goodsupdate$', typeviews.goodsupdate, name="goodsupdate"),
 

 
    
]
