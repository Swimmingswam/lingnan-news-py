"""Defines url patterns for news_app."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page.
    url(r'^$', views.index, name='index'),
    url(r'^konwladge$',views.konwladge,name="konwladge"),
    url(r'^group$',views.group,name="group"),
    url(r'^news$',views.news,name="news"),
    url(r'^news/(?P<new_id>\d+)/$',views.new,name='new'),
    url(r'^culture$',views.culture,name="culture"),
    url(r'^beatiful$',views.beatiful,name="beatiful"),
    url(r'^home$',views.home,name="home"),
    url(r'^come$',views.come,name="come"),
    url(r'^old$',views.old,name="old"),
    url(r'^talk$',views.talk,name="talk"),
    url(r'^comment$',views.comment,name="comment"),
]
app_name = 'news_app'
