from django.conf.urls import url
from . import views
from .views import WritePostView
urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.postList, name='postList'),
    url(r'^readpost/(?P<id>\d+)/$',views.readPost, name='readPost'),
    url(r'^writePost/$', views.WritePostView.as_view(), name='writePost'),
    url(r'^editPost/(?P<id>[0-9]+)/$', views.editPost, name='editPost'),
]
