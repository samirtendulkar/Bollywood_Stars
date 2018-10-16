from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.PostView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.PostDetail.as_view(), name='detail'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post_add/$', views.PostCreate.as_view(), name='post_add'),
    url(r'^(?P<pk>\d+)/post_edit/$', views.PostUpdate.as_view(), name='post_edit'),
    url(r'^(?P<pk>\d+)/post_delete/$', views.PostDelete.as_view(), name='post_delete'),
    url(r'^post_drafts/$', views.PostDraftList.as_view(), name='post_drafts'),
    url(r'^(?P<pk>\d+)/post_publish/$', views.post_publish, name='post_publish'),
    url(r'^(?P<pk>\d+)/add_comment/$', views.add_comment_to_post, name='add_comment'),
    url(r'^(?P<pk>\d+)/approve_comment/$', views.approve_comment, name='approve_comment'),
    url(r'^(?P<pk>\d+)/remove_comment/$', views.remove_comment, name='remove_comment'),
]