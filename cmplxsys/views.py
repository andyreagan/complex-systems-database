from django.shortcuts import render
from django.shortcuts import get_object_or_404
# from django.http import Http404
from django.http import HttpResponse
from django.views.generic import View
# from django.core.context_processors import csrf
# from django.template import Context

from mysite.settings import STATIC_ROOT

from cmplxsys.models import Person,Paper

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

class paperfull(View):
     # return all of the annotations for a book
    def get(self, request, paper):
        dbentry = Paper.objects.filter(id=paper)
        if len(dbentry) > 0:
            
            # paper_list = dbentry[0].paper_set.all().order_by('-year')
            # press_list = dbentry[0].press_set.all()
            # project_list = dbentry[0].project_set.all()
            
            # note that these are backward!
            # (oops)
            author_list = dbentry[0].authors.all()
            press_list = dbentry[0].press_set.all()
            
            return render(request, 'cmplxsys/paperfull.html',
                          {"paper": dbentry[0],
                           "author_list": author_list,
                           "press_list": press_list, }
                         )
        else:
            return HttpResponse('<p>Paper ID=<strong>{0}</strong> not found in our database</p>'.format(paper))
