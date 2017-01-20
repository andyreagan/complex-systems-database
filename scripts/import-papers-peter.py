import sys, os
# sys.path.append('/home/cmplxsys/cmplxsys')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

sys.path.append('/users/c/m/cmplxsys/www-root/db/complex-systems-database/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.conf import settings

from cmplxsys.models import *
from datetime import datetime,tzinfo
class GMT1(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=1) + self.dst(dt)
    def dst(self, dt):
        # DST starts last Sunday in March
        d = datetime(dt.year, 4, 1)   # ends last Sunday in October
        self.dston = d - timedelta(days=d.weekday() + 1)
        d = datetime(dt.year, 11, 1)
        self.dstoff = d - timedelta(days=d.weekday() + 1)
        if self.dston <=  dt.replace(tzinfo=None) < self.dstoff:
            return timedelta(hours=1)
        else:
            return timedelta(0)
    def tzname(self,dt):
         return "GMT +1"
gmt1 = GMT1()

from subprocess import call

from urllib import urlopen
from os.path import isfile,isdir

from django.core.files import File
            
if __name__ == "__main__":
    f = open("papers.txt","r")
    papers = [dict()]
    for line in f:
        # print(line)
        if line == "\n":
            papers.append(dict())
        else:
            data = line.rstrip().split("::")
            # print(data)
            papers[-1][data[0]] = data[1]
    print(len(papers))
    # print(papers)
    # print(papers[0])
    # print(papers[-1])
    matches = 0
    for paper in papers:
        if "title" in paper:
            p = Paper.objects.filter(title=paper["title"])
            # print(len(p))
            if len(p) == 1:
                matches += 1
                match = p[0]
                if "year" in paper:
                    match.year = paper["year"]
                    if match.sort_date < datetime(1951,1,1,tzinfo=gmt1):
                        match.sort_date = datetime(int(paper["year"]),1,1)
                if "googlescholarlink" in paper:
                    match.googlescholarlink = paper["googlescholarlink"]
                if "reprintlink" in paper:
                    match.preprintlink = paper["reprintlink"]
                if "supplementarylink" in paper:
                    match.supplementarylink = paper["supplementarylink"]
                if "onlineappendices" in paper:
                    match.onlineappendices = paper["onlineappendices"]
                if "journalpagelink" in paper:
                    match.journalpagelink = paper["journalpagelink"]
                if "arxivlink" in paper:
                    match.arxivlink = paper["arxivlink"]
                if "status" in paper:
                    match.status = paper["status"]
                if "journal" in paper:
                    match.journal = paper["journal"]
                if "volume" in paper:
                    match.volume = paper["volume"]
                if "pages" in paper:
                    match.pages = paper["pages"]
                if "abstract" in paper:
                    match.HTMLabstract = paper["abstract"]
                if "latexabstract" in paper:
                    match.abstract = paper["latexabstract"]
                if "bibref" in paper:
                    match.bibref = paper["bibref"]
                match.save()
            else:
                print(paper["title"])
    print(matches)
    

