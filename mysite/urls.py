# /usr/share/nginx/wiki/mysite/mysite/urls.py

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# not using, out of date
# import likes

from mysite import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('cmplxsys.urls',namespace='cmplxsys')),
    url(r'^admin/', include(admin.site.urls)),
    # either the trailing slash, or not, we'll allow it, using [/]*$ didn't work as expected?
    # url(r'^people/([A-Za-z\-]*?)/([A-Za-z]*?)/$', views.people.as_view()),
    url(r'^people/([A-Za-z\-]*?)/$', views.peoplelists.as_view()),
    url(r'^people/([A-Za-z\-]*?)/([A-Za-z]+?)$', views.people.as_view()),
    url(r'^people/([A-Za-z\-]*?)/([A-Za-z]+?)/$', views.people.as_view()),
    # url(r'^people/([A-Za-z\-]*?)/([A-Za-z]*?)', views.people.as_view()),
    # url(r'^people/([A-Za-z\.]*?)/$', views.people.as_view()),
    url(r'^research/publications/$', views.paperlist.as_view()),
    url(r'^research/publications/([A-Za-z0-9]+?)$', views.paper.as_view()),
    url(r'^research/publications/([A-Za-z0-9]+?)/$', views.paper.as_view()),
    url(r'^research/press/$', views.presslist.as_view()),
    url(r'^(.*)', views.rapidweaver.as_view()),
)

def static_filetype(filetype, view='django.views.static.serve', **kwargs):
    """
    Helper function to return a URL pattern for serving files in debug mode.
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns = patterns('',
        # ... the rest of your URLconf goes here ...
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    """
    # No-op if not in debug mode or an non-local prefix
    return patterns('',
        url(r'^(?P<path>.*%s)$' % filetype, view, kwargs=kwargs),
    )

# # load the static files if in debug
from settings import DEBUG
if DEBUG:
    from django.conf.urls.static import static
    from django.views.static import serve
    from django.conf import settings
    urlpatterns = (
        static(
            settings.STATIC_URL,
            document_root=settings.STATIC_ROOT
        ) + static(
            '/rw_common',
            document_root='/users/c/m/cmplxsys/www-root/templatery/rw_common'
        ) + static(
            '/index_files',
            document_root='/users/c/m/cmplxsys/www-root/templatery/index_files'
        ) + static_filetype(
	    'png',
            document_root='/users/c/m/cmplxsys/www-root/templatery/'
        ) + static_filetype(
            'jpg',
            document_root='/users/c/m/cmplxsys/www-root/templatery/'
        ) + static_filetype(
            'css',
            document_root='/users/c/m/cmplxsys/www-root/templatery/'
        ) + static_filetype(
            'js',
            document_root='/users/c/m/cmplxsys/www-root/templatery/'
        ) + urlpatterns
    )
    





