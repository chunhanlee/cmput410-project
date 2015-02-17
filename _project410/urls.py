from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
import friends.views
import author.views
import friendrequest.views
from django.conf.urls.static import static
>>>>>>> brian

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '_project410.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', author.views.mainPage, name='mainPage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^friends/', friends.views.index, name='index'),
    url(r'^author/', include('author.urls')),
    url(r'^friendrequest/', friendrequest.views.index, name='index'),
    
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )