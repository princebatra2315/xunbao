from django.conf.urls import url
from . import views

app_name = 'myapp'

urlpatterns = [
    # xunbao/
    url(r'^$', views.index, name='index'),

    # xunbao/login/
    url(r'^login/$', views.index, name='login'),

    # xunbao/leaderboard/
    url(r'^leaderboard/$', views.leaderboard, name='leaderboard'),

    # logout
    url(r'^logout/$', views.my_logout, name='logout'),

    # /xunbao/developers/
    url(r'^developers/$', views.developers, name='developers'),
    
    #api's
    url(r'^logs/$', views.logs_data),
]
