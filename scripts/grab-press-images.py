import sys, os
# sys.path.append('/home/cmplxsys/cmplxsys')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

sys.path.append('/users/c/m/cmplxsys/www-root/db/complex-systems-database/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.conf import settings

from cmplxsys.models import *
from datetime import datetime

from subprocess import call

from urllib import urlopen
from os.path import isfile,isdir

from django.core.files import File

def find_candidate_list():
    the_list = []
    # reconvert all of the current images
    for p in Press.objects.all():
        if len(p.imagelink) > 0 and not p.image:
            print(p.imagelink)
            image_filename = "".join(list(p.imagelink.split("/")[-1])[-10:])
            print(image_filename)
            if not isfile("/users/c/m/cmplxsys/www-root/static/media/press/"+image_filename):
                try:
                    f = open("/users/c/m/cmplxsys/www-root/static/media/press/"+image_filename,"wb")
                    f.write(urlopen(p.imagelink).read())
                    f.close()
                except:
                    print("image not found for:")
                    print(p.title)
                    raise
            else:
                reopen = open("/users/c/m/cmplxsys/www-root/static/media/press/"+image_filename, "rb")
                django_file = File(reopen)
                p.image.save(image_filename,django_file,save=True)
                p.save()
                print("saved!")
        if p.image:
            print(p.image)
            
            
if __name__ == "__main__":
    my_list = find_candidate_list()

