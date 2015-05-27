import sys, os
# sys.path.append('/home/cmplxsys/cmplxsys')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

sys.path.append('/users/c/m/cmplxsys/www-root/db/complex-systems-database/testsite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.conf import settings

from cmplxsys.models import *
from datetime import datetime

def something():
    [di,hi]=sys.argv[1].split(',')
    dates = map(int,di.split('-'))
    d = datetime.datetime(dates[0],dates[1],dates[2])
    v = float(hi)
    h = Happs(date=d,value=v)
    h.save()

def addcourses():
    f = open('imports/tblCourse.csv','r')
    courses = [[x.rstrip('",').lstrip('",') for x in line.rstrip().split(',"')] for line in f]
    f.close
    for c in courses:
        print c
        print len(c)
        if len(c) > 2:
            if len(c) > 3:
                link = c[3]
            else:
                link = ''
            num,title,desc = c[0:3]
            C = Course(shortcode=num,title=title,description=desc,logline='',url=link,nextoffering=datetime.now())
            print C
            C.save()

def addprojects():
    f = open('imports/tblProject.csv','r')
    courses = [[x.rstrip('",').lstrip('",') for x in line.rstrip().split(',"')] for line in f]
    f.close
    for c in courses:
        print c
        print len(c)
        if len(c[0]) > 1:
            title= c[0]
            if len(c) > 1:
                desc = c[1]
            else:
                desc = ''
            C = Project(title=title,description=desc)
            print C
            C.save()


def addpress():
    f = open('imports/tblMedia.csv','r')
    courses = [[x.rstrip('",').lstrip('",') for x in line.rstrip().split('@')] for line in f]
    f.close
    for c in courses:
        # print c
        print len(c)
        if len(c[0]) > 6:
            url,author,d,title,desc,imglink,org = c
            try:
                date = datetime.strptime(d.replace(' 0', ' '),'%B %d, %Y')
            except:
                try:
                    date = datetime.strptime(d,'%y%m%d')
                except:
                    date = datetime.strptime(d.replace(' 0', ' '),'%b %d, %Y ')
            print date
            C = Press(url=url,author=author,date=date,title=title,description=desc,imagelink=imglink,organization=org)
            # print C
            C.save()

def addprojectstopress():
    f = open('imports/tblProjectMedia.csv','r')
    courses = [[x.rstrip('",').lstrip('",') for x in line.rstrip().split(',"')] for line in f]
    f.close
    for c in courses:
        # print c
        # print len(c)
        if len(c) > 2:
            proj,url,fav = c
            print url
            C = Press.objects.filter(url=url)[0]
            P = Project.objects.filter(title=proj)[0]
            print C.projects
            print P
            C.projects.add(P)
            # print C.projects
            C.save()

def fixpaperabstracts():
    f = open('imports/tblPaper.csv','r')
    courses = [[x.rstrip('",').lstrip('",') for x in line.rstrip().split(':')] for line in f]
    f.close
    for c in courses:
        # print c
        # print len(c)
        if len(c) > 2:
            # pass
            title,nothing,nothingelse,abst = c[0:4]
            # print title
            # print abst
            # print moreabst
            # print abst
            if len(c) > 17:
                # print c[4:len(c)-17+4]
                a = c[4:]
                i = 0
                while a[i] not in ['http','Published','https','Unpublished']:
                    if len(a[i]) > 0:
                        abst = ':'.join([abst,a[i]])
                    i += 1
                abst = abst.lstrip(":")
                # print abst
            # print url
            C = Paper.objects.filter(title__exact=title)
            print len(C)
            if len(C) == 0:
                print title
            # P = Project.objects.filter(title=proj)[0]
            # print C.projects
            # print P
            # C.abstract = abst
            # print C.projects
            # C.save()

def fixpaperabstractsnew():
    f = open('imports/tblPaperNew.csv','r')
    f.readline()
    courses = [[x.rstrip('",').lstrip('",') for x in line.rstrip().split('@')] for line in f]
    f.close
    for c in courses:
        # print c
        # print len(c)
        if len(c) > 2:
            # pass
            title,abst = c[0:2]
            # print title
            # print abst
            C = Paper.objects.filter(title__exact=title)
            if len(C) == 1:
                C[0].abstract = abst
                C[0].save()
                

if __name__ == '__main__':
    print 'hey there'
    # addcourses()
    # addprojects()
    # addpress()
    # addprojectstopress()
    # fixpaperabstracts()
    # fixpaperabstractsnew()


