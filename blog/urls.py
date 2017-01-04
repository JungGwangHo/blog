from django.conf.urls import include, url
from django.contrib import admin
#로그인, 회원가입
from django.views.generic import TemplateView
from myblog.views import DuplicationCheck
#summernote
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/', include('myblog.urls')),
    ## 로그인, 회원가입
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/',}, name='logout_url'),
    url(r'^signup/$','myblog.views.signup', name='signup'),
    url(r'^signup_ok/$',TemplateView.as_view(template_name='registration/signup_ok.html'), name='signup_ok'),
    url(r'^duplcheck$', DuplicationCheck.as_view(), name='duplcheck'),
    url(r'^summernote/', include('django_summernote.urls')),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
