from django.shortcuts import render
from django.shortcuts import get_object_or_404
# from django.http import Http404
from django.http import HttpResponse
from django.views.generic import View
# from django.core.context_processors import csrf
# from django.template import Context

from mysite.settings import STATIC_ROOT

from cmplxsys.models import Person

# from django.views.decorators.csrf import csrf_exempt, csrf_protect
# from django.core import serializers

# import csv
# import subprocess
# import codecs
# import json
# import datetime

class personfull(View):
     # return all of the annotations for a book
    def get(self, request, person):
        dbentry = Person.objects.filter(uname=person)
        if len(dbentry)>0:
            paper_list = dbentry[0].paper_set.all()
            return render(request, 'cmplxsys/personfull.html',{"person": dbentry[0], "paper_list": paper_list})
        else:
            return HttpResponse('<p><strong>{0}</strong> not found in our database</p>'.format(person))


