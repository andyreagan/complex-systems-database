import sys, os
# sys.path.append('/home/cmplxsys/cmplxsys')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

sys.path.append('/users/c/m/cmplxsys/www-root/db/complex-systems-database/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.conf import settings

from cmplxsys.models import *
from datetime import datetime

from subprocess import call

# # fix the paper default image to the actual blank one
# for p in Paper.objects.all():
#     print(p.image)
#     if p.image == "paper/blank.png":
#         p.image = "papers/blank.png"
#         p.save()


# # wget'ed all of the images from http://www.uvm.edu/~jfedorko/Square,%20Backgroundless,%20and%20named%20Photos/
# # they're in the images folder inside scripts

# # loop through and add images to all people that have them processed
# for p in Person.objects.all():
#     print(p.fullname)

my_matches = []

a = os.listdir("images")
print(a)
print("there are this many:")
print(len(a))
for image in a:
    # print("-"*30)
    name = image[:-4]
    # print(name)
    lastname = name[1:]
    # print(lastname)
    matches = Person.objects.filter(fullname__icontains=lastname)
    if len(matches) > 0:
        my_matches.append(matches[0])
        # print("match found")
        # if len(matches) > 1:
        #     print(name)
        #     print("more than 1 match!!")
        #     for m in matches:
        #         print(m.fullname)
        # command = datetime.now().strftime("convert -geometry 163x -colorspace Gray ~/www-root/db/complex-systems-database/scripts/images/{0} ~/www-root/static/media/people/%Y-%m-%d-%H-%M-{1}.png".format(image,matches[0].uname))
        # matches[0].image =  datetime.now().strftime("people/%Y-%m-%d-%H-%M-{1}.png".format(image,matches[0].uname))
        # matches[0].save()
        # print(command)
        # call(command,shell=True)
    # else:
    # #     print(name)
    #     print("no match!!")

# # fix all of the defaults    
# for p in Person.objects.all():
#     print(p.image)
#     if p.image == "person/blank.png":
#         p.image = "people/blank.png"
#         p.save()

# reconvert all of the current images
for p in Person.objects.all():
    # print(p.image)
    if not p.image == "person/blank.png":
        if p not in my_matches:
            command = datetime.now().strftime("convert -geometry 163x -colorspace Gray ~/www-root/static/media/{0} ~/www-root/static/media/people/%Y-%m-%d-%H-%M-{1}.png".format(p.image,p.uname))
            call(command,shell=True)
            p.image = datetime.now().strftime("people/%Y-%m-%d-%H-%M-{0}.png".format(p.uname))
            p.save()
            # print("{0}".format(p.id))
            print("{0},{1}".format(p.uname,p.fullname))

# convert -geometry 163x -colorspace Gray $file $outfile

