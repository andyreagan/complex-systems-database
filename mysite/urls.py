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

# # load the static files if in debug
# from settings import DEBUG
# if DEBUG:
#     from django.conf.urls.static import static
#     from django.conf import settings
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# # set the static first
# from django.conf.urls.static import static
# from django.conf import settings
# from mysite import views
# urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static('rw_common/', document_root='/users/c/m/cmplxsys/www-root/rw_common/')+patterns('',
#     url(r'^', include('cmplxsys.urls',namespace='cmplxsys')),
#     url(r'^admin/', include(admin.site.urls)),
#     # url(r'^(.*)', include(admin.site.urls)),
#     url(r'^(.*)', views.rapidweaver.as_view()),
# )


    





