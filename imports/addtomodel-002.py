import sys, os
# sys.path.append('/home/cmplxsys/cmplxsys')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

sys.path.append('/users/c/m/cmplxsys/www-root/db/complex-systems-database/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.conf import settings

from cmplxsys.models import *
from datetime import datetime

import codecs

def relink_papers():
    Order.objects.all().delete()
    f = codecs.open("save.csv","r","utf-8")
    for i in range(634):
        line = f.readline()
    line = f.readline()
    print(line)
    line = line.rstrip().split(':::')
    author = Person.objects.get(uname=line[1])
    paper = Paper.objects.get(title=line[0])
    a = Order(author=author,paper=paper,order=0)
    a.save()
    for line in f:
        line = line.rstrip().split(':::')
        author = Person.objects.get(uname=line[1])
        paper = Paper.objects.get(title=line[0])
        a = Order(author=author,paper=paper,order=0)
        a.save()
    f.close()
    
if __name__ == '__main__':
    print 'hey there'
    relink_papers()
    me = Person.objects.get(uname="areagan")
    print(me.paper_set.all())


