from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
# from django.http import Http404
from django.http import HttpResponse
from django.views.generic import View
# from django.core.context_processors import csrf
# from django.template import Context

from mysite.settings import STATIC_ROOT

from cmplxsys.models import Person,Paper,Project,Press

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
            peoplelist = Person.objects.filter(core_team=True).order_by('core_team_order')
        elif group == "associated-faculty":
            peoplelist = Person.objects.filter(associated_faculty=True).order_by('core_team_order')
        elif group == "postdocs":
            peoplelist = Person.objects.filter(post_doc=True)
        elif group == "students":
            peoplelist = Person.objects.filter(current_student=True)
        elif group == "alumni":
            peoplelist = Person.objects.filter(alumni=True)            
        else:
            peoplelist = Person.objects.all()
        # this will render the template for that team
        return render(request, 'mysite/people/'+group+"/index.html",{"people":peoplelist})

class people(View):
    def get(self, request, group, username):
        if request.path[-1] == "/":
            return redirect("/people/"+group+"/"+username)
        person = get_object_or_404(Person,uname=username)
        # paper_list = person.paper_set.all().order_by('-sort_date')
        # author_lists = [[model_to_dict(author,fields=["fullname"]) for author in paper.authors.all().order_by('order')] for paper in paper_list]
        # for i,paper in enumerate(payload["papers"]):
        #     paper["authors"] = author_lists[i]
        
        all_press_list = [paper.press_set.all() for paper in person.paper_set.all()]
        first_auth_press_list = [order.paper.press_set.all() for order in person.order_set.filter(order=0)]
        selected_press_list = person.press_set.all()

        return render(request, 'mysite/people/core-team/index.html',{
            "p":person,
            # "paper_lists":paper_lists,
            # "author_lists":author_lists,
            "all_press_list":all_press_list,
            "first_auth_press_list":first_auth_press_list,
            "selected_press_list":selected_press_list,})

class paperlist(View):
    def get(self, request):
        most_recent_papers = Paper.objects.all()
        authors = Person.objects.all()
        return render(request, 'mysite/research/publications/index.html',{"papers": most_recent_papers, "authors":authors})

class paper(View):
    def get(self, request, bibref):
        if request.path[-1] == "/":
            return redirect("/research/publications/"+bibref)
        p = get_object_or_404(Paper,bibref=bibref)
        sorted_order = [x.id for x in Paper.objects.all().order_by('-sort_date')].index(p.id)
        rand_p = Paper.objects.all().order_by('?')[0]
        if sorted_order == 0:
            next_text = "Cycle back to oldest paper"
            prev_text = "Less recent"
        elif sorted_order == 0:
            next_text = "More recent"
            prev_text = "Cycle to most recent paper"
        else:
            next_text = "More recent"
            prev_text = "Less recent"
        next_p = Paper.objects.all()[(sorted_order-1+len(Paper.objects.all())) % len(Paper.objects.all())]
        prev_p = Paper.objects.all()[(sorted_order+1) % len(Paper.objects.all())]
        return render(request, 'mysite/research/publications/index.html',{"paper": p,"rand":rand_p,"next_p":next_p,"prev_p":prev_p,"next_text":next_text,"prev_text":prev_text})

class presslist(View):
    def get(self, request):
        # should sort automatically
        presslist = Press.objects.all()[:50]
        return render(request, 'mysite/research/press/index.html',{"presslist": presslist})
