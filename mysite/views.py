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

class rapidweaver(View):
    def get(self, request, url):
        if len(url) > 0:
            if url[-1] == "/":
                url+="index"
        elif url == "":
            return render(request, 'mysite/index.html',{})
        if ".html" in url:
            return render(request, 'mysite/'+url,{})
        else:
            return render(request, 'mysite/'+url+".html",{})

class peoplelists(View):
    def get(self, request, group):
        if group == "core-team":
            # go get all the core team people, pass that list off to the template
            peoplelist = []
        # this will render the template for that team
        return render(request, 'mysite/'+group+"/index.html",{"people":peoplelist})

class people(View):
    def get(self, request, group, username):
        person = get_object_or_404(Person,uname=username)
        paper_list = person.paper_set.all().order_by('-sort_date')
        author_lists = [[model_to_dict(author,fields=["fullname"]) for author in paper.authors.all().order_by('order')] for paper in paper_list]
        # for i,paper in enumerate(payload["papers"]):
        #     paper["authors"] = author_lists[i]
        
        all_press_list = [paper.press_set.all() for paper in paper_list]
        first_auth_press_list = [order.paper.press_set.all() for order in person.order_set.filter(order=0)]
        selected_press_list = person.press_set.all()

        return render(request, 'mysite/people/core-team/index.html',{
            "fullname": "Test User "+username+" from "+group,
            "person":person,
            "paper_list":paper_list,
            "author_lists":author_lists,
            "all_press_list":all_press_list,
            "first_auth_press_list":first_auth_press_list,
            "selected_press_list":selected_press_list,})


