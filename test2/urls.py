from django.conf.urls import url, include
from . import views

urlpatterns= [
    url(r'^games/sadari/$', views.enter_sadari, name='enter_sadari'),
    url(r'^etc/community/$', views.enter_community, name='enter_community'),
    url(r'^etc/community/post/(?P<pk>\d+)/$', views.community_post_detail, name='community_post_detail'),
    url(r'^etc/community/post/new/$', views.community_post_new, name='community_post_new'),
    url(r'^etc/community/post/(?P<pk>\d+)/edit/$', views.community_post_edit, name='community_post_edit'),



    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^member_info/$', views.member_info, name='member_info'),

    url(r'^$', views.Login, name='login'),
    url(r'^post/$', views.post_new, name='post_new'),
    url(r'^home/$', views.home, name='home'),

        ]
