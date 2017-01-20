import sys, os
# sys.path.append('/home/cmplxsys/cmplxsys')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

sys.path.append('/users/c/m/cmplxsys/www-root/db/complex-systems-database/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.conf import settings

from cmplxsys.models import *
from datetime import datetime

from time import sleep
import random

for paper in Paper.objects.all():
    # sleep(random.random()/10.0)
    if paper.HTMLabstract == '':
        paper.HTMLabstract = paper.abstract
    if paper.year == 1950 and len(paper.arxivlink) > 0:
        year = "".join(list(paper.arxivlink.split('.')[-2])[-4:-2])
        try:
            year = int(year)
            if year < 16:
                year+= 2000
            else:
                year+= 1900
            paper.year = year
        except:
            print("failed to convert data for {0}".format(paper.title))
    if not paper.titlelink and paper.arxivlink:
        paper.titlelink = paper.arxivlink
    if not paper.titlelink and paper.journalpagelink:
        paper.titlelink = paper.journalpagelink
    if not paper.titlelink and paper.preprintlink:
        paper.titlelink = paper.preprintlink
    paper.save()


