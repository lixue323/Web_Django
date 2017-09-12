from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^show$',views.show,name='show'),
    url(r'^content$',views.content,name='content'),
    url(r'^denglu1$',views.denglu1,name='denglu1'),
    url(r'^buycar$',views.buycar,name='buycar'),
]
