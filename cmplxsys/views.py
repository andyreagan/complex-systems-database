from django.shortcuts import render
from django.shortcuts import get_object_or_404
# from django.http import Http404
from django.http import HttpResponse
from django.views.generic import View
# from django.core.context_processors import csrf
# from django.template import Context

from mysite.settings import STATIC_ROOT

from cmplxsys.models import Person,Paper,Project

# from django.views.decorators.csrf import csrf_exempt, csrf_protect
# from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from json import dumps

# import csv
# import subprocess
# import codecs
# import json
# import datetime

class bibtex(View):
    def get(self, request, paper):
        dbentry = get_object_or_404(Paper,id=paper)
        authors = dbentry.authors.all().order_by('order__order')
        return render(request, 'cmplxsys/bibtex.html',{"paper": dbentry, "authors": authors})
        
class personfull(View):
     # return all of the annotations for a book
    def get(self, request, person):
        dbentry = get_object_or_404(Person,uname=person)
        payload = model_to_dict(dbentry)
        paper_list = dbentry.paper_set.all().order_by('-sort_date')
        author_lists = [[model_to_dict(author,fields=["fullname"]) for author in paper.authors.all().order_by('order')] for paper in paper_list]
        payload["papers"] = [model_to_dict(paper) for paper in paper_list]
        for i,paper in enumerate(payload["papers"]):
            paper["authors"] = author_lists[i]
        
        all_press_list = [list(map(model_to_dict,paper.press_set.all())) for paper in paper_list]
        first_auth_press_list = [list(map(model_to_dict,order.paper.press_set.all())) for order in dbentry.order_set.filter(order=0)]
        selected_press_list = list(map(model_to_dict,dbentry.press_set.all()))

        payload["press"] = all_press_list
        payload["press_firstauthor"] = first_auth_press_list
        payload["press_selected"] = selected_press_list
        
        # project_list = dbentry.project_set.all()
        # # note that these are backward!
        # # (oops)
        # teaching_list = dbentry.courses_taken.all()
        # class_list = dbentry.courses_taught.all()
        # funding_list = dbentry.funding_set.all()
        
        return HttpResponse(dumps(payload,cls=DjangoJSONEncoder), content_type="application/json")

# paperfull was not used
    # return HttpResponse('<p>Paper ID=<strong>{0}</strong> not found in our database</p>'.format(paper))


class paperembed(View):
     # return all of the annotations for a book
    def get(self, request, paper):
        dbentry = get_object_or_404(Paper,id=paper)

        authors = dbentry.authors.all().order_by('order__order')
        press_list = dbentry.press_set.all()
        # author_list_1 = "";
        # for i,author in enumerate(authors):
        #     author_list_1 += author.fullname
        #     if i<len(authors)-1:
        #         author_list_1 += ", "
        author_list_2 = ", ".join([author.fullname for author in authors])
        return render(request,
                      'cmplxsys/paperembed.html',
                      {"paper": dbentry,
                       "author_list": author_list_2,})
    
class projectpressembed(View):
     # return all of the annotations for a book
    def get(self, request, project):
        my_project = get_object_or_404(Project,title__startswith=project).press_set.order_by('-date')
        for press in my_project:
            press.monthdate = press.date.strftime("%B %Y")
        return render(request,
                      'cmplxsys/manypressembed.html',
                      {"press_list": my_project,})
        
