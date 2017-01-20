# urls.py
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView,RedirectView

from tastypie.api import Api
from cmplxsys.api import PersonResource, PaperResource, BasicPaperResource, BasicFundingResource, BasicPressResource, BasicProjectResource, BasicPersonResource, RecentPressResource
from cmplxsys import views

v1_api = Api(api_name='v1')
v1_api.register(PersonResource())
v1_api.register(BasicPersonResource())
v1_api.register(BasicPaperResource())
v1_api.register(PaperResource())
v1_api.register(RecentPressResource())
# v1_api.register(BasicFundingResource())
# v1_api.register(BasicPressResource())
# v1_api.register(BasicProjectResource())

urlpatterns = patterns('',
    # The normal jazz here...
    # (r'^blog/', include('myapp.urls')),
    url(r'^index/',
        TemplateView.as_view(template_name='cmplxsys/index.html'),
        name='index'),
    url(r'^person/full/(?P<person>[\w]+)/$',views.personfull.as_view()),
    url(r'^paper/full/(?P<paper>[\w]+)/$',views.paperfull.as_view()),
    url(r'^paper/embed/(?P<paper>[\w]+)/$',views.paperembed.as_view()),
    url(r'^press/embed/project/(?P<project>[\w\.]+)/$',views.projectpressembed.as_view()),
    url(r'^bibgen/(?P<paper>[0-9]+)/$',views.bibtex.as_view()),
    (r'^api/', include(v1_api.urls)),
)


