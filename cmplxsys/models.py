from django.db import models
from datetime import datetime

def rename_files_person(instance,filename):
    return datetime.now().strftime("people/%Y-%m-%d-%H-%M-{0}".format(filename))

# Create your models here.
# a model for the people
# pointed to by courses (twice), papers, projects, press, funding
# which is everything else
class Person(models.Model):
    # username
    uname = models.CharField(max_length=20)
    # eventually can build a model for affiliations (VACC, UVM, CSYS, CS, MATH, etc)
    # but bigger fish to fry right now
    institution = models.CharField(max_length=200, default="University of Vermont")
    affiliation0 = models.CharField(max_length=200, default="Department of Mathematics and Statistics")
    role0 = models.CharField(max_length=200, default="Professor",)
    affiliation1 = models.CharField(max_length=200, null=True, blank=True, default="",)
    role1 = models.CharField(max_length=200, null=True, blank=True, default="",)
    affiliation2 = models.CharField(max_length=200, null=True, blank=True, default="",)
    role2 = models.CharField(max_length=200, null=True, blank=True, default="",)
    affiliation3 = models.CharField(max_length=200, null=True, blank=True, default="",)
    role3 = models.CharField(max_length=200, null=True, blank=True, default="",)
    affiliation4 = models.CharField(max_length=200, null=True, blank=True, default="",)
    role4 = models.CharField(max_length=200, null=True, blank=True, default="",)
    secondaryaffiliation0 = models.CharField(max_length=200, null=True, blank=True, default="",)
    secondaryrole0 = models.CharField(max_length=200, null=True, blank=True, default="",)
    secondaryaffiliation1 = models.CharField(max_length=200, null=True, blank=True, default="",)
    secondaryrole1 = models.CharField(max_length=200, null=True, blank=True, default="",)
    secondaryaffiliation2 = models.CharField(max_length=200, null=True, blank=True, default="",)
    secondaryrole2 = models.CharField(max_length=200, null=True, blank=True, default="",)
    secondaryaffiliation3 = models.CharField(max_length=200, null=True, blank=True, default="",)
    secondaryrole3 = models.CharField(max_length=200, null=True, blank=True, default="",)
    secondaryaffiliation4 = models.CharField(max_length=200, null=True, blank=True, default="",)
    secondaryrole4 = models.CharField(max_length=200, null=True, blank=True, default="",)

    blurb = models.TextField(null=True, blank=True, default="",)
    fullname = models.CharField(max_length=200)
    # split up name is optional, for now
    first = models.CharField(max_length=200, null=True, blank=True, default="")
    middle = models.CharField(max_length=200, null=True, blank=True, default="")
    last = models.CharField(max_length=200, null=True, blank=True, default="")
    sur = models.CharField(max_length=200, null=True, blank=True, default="")
    webpage = models.CharField(max_length=200, null=True, blank=True, default="")
    linkedin = models.CharField(max_length=200, null=True, blank=True, default="")
    twitter = models.CharField(max_length=200, null=True, blank=True, default="")
    strava = models.CharField(max_length=200, null=True, blank=True, default="")
    facebook = models.CharField(max_length=200, null=True, blank=True, default="")
    youtube = models.CharField(max_length=200, null=True, blank=True, default="")
    vine = models.CharField(max_length=200, null=True, blank=True, default="")
    instagram = models.CharField(max_length=200, null=True, blank=True, default="")
    scholar = models.CharField(max_length=200, null=True, blank=True, default="")
    github = models.CharField(max_length=200, null=True, blank=True, default="")
    bitbucket = models.CharField(max_length=200, null=True, blank=True, default="")
    stackoverflow = models.CharField(max_length=200, null=True, blank=True, default="")
    plus = models.CharField(max_length=200, null=True, blank=True, default="")
    pinterest = models.CharField(max_length=200, null=True, blank=True, default="")

    image = models.FileField(upload_to=rename_files_person,default="person/blank.png",
                             help_text="Timestamp will automatically be added.")

    def __unicode__(self):
        return self.fullname

    class Meta:
        ordering = ('uname',)
        # order_with_respect_to = 'order__order'

def rename_files_project(instance,filename):
    return datetime.now().strftime("projects/%Y-%m-%d-%H-%M-{0}".format(filename))        

# projects
# point to people
# pointed to by papers, funding
class Project(models.Model):
    title = models.CharField(max_length=500, default="Earth shattering project.")
    description = models.TextField(null=True, blank=True)
    people = models.ManyToManyField(Person)

    image = models.FileField(upload_to=rename_files_project,default="project/blank.png",
                             help_text="Timestamp will automatically be added.")

    def __unicode__(self):
        return self.title

# funding
# pointed to by papers
# points to projects, people
class Funding(models.Model):
    title = models.CharField(max_length=500, default="100M Award.")
    url = models.CharField(max_length=2000, default="http://www.nsf.gov")
    startdate = models.DateTimeField('date begins')
    enddate = models.DateTimeField('date ends')
    shortdescription = models.CharField(max_length=1000, null=True, blank=True)
    longdescription = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=200, null=True, blank=True)

    project = models.ManyToManyField(Project, blank=True)
    people = models.ManyToManyField(Person, blank=True)

    def __unicode__(self):
        return self.title

# courses
# papers will point to them
# they point to students and teachers (both Persons)
class Course(models.Model):
    shortcode = models.CharField(max_length=500, default="CSYS 500.")
    title = models.CharField(max_length=500, default="Learn all the things.")
    description = models.CharField(max_length=2000, default="")
    logline = models.CharField(max_length=500, default="")
    url = models.CharField(max_length=2000, default="http://www.uvm.edu/~bagrow")
    nextoffering = models.DateTimeField('date offered next')
    numtimesoffered = models.CharField(max_length=200, null=True, blank=True)
    imagelink = models.CharField(max_length=200, null=True, blank=True)

    students = models.ManyToManyField(Person,related_name='courses_taught', blank=True)
    teachers = models.ManyToManyField(Person,related_name='courses_taken')

    def __unicode__(self):
        return self.shortcode


def rename_files_paper(instance,filename):
    return datetime.now().strftime("papers/%Y-%m-%d-%H-%M-{0}".format(filename))            
    
# papers
# point to authors, projects, funding (for direct funding), course
# pointed to by press
class Paper(models.Model):
    title = models.CharField(max_length=500)
    logline = models.CharField(max_length=500, null=True, blank=True,)
    abstract = models.TextField(default="There are none.",help_text="LaTeX format")
    HTMLabstract = models.TextField(default="There are none.<br>",help_text="HTML format")
    img = models.CharField(max_length=200, null=True, blank=True,)
    status = models.CharField(max_length=200)
    arxiv = models.CharField(max_length=200, null=True, blank=True)
    arxivpw = models.CharField(max_length=200, null=True, blank=True)
    journal = models.CharField(max_length=200, null=True, blank=True)
    volume = models.CharField(max_length=200, null=True, blank=True)
    pages = models.CharField(max_length=200, null=True, blank=True)
    year = models.IntegerField(default=1950)
    googlescholarlink = models.CharField(max_length=200, null=True, blank=True)
    preprintlink = models.CharField(max_length=200, null=True, blank=True)
    supplementarylink = models.CharField(max_length=200, null=True, blank=True)
    onlineappendices = models.CharField(max_length=200, null=True, blank=True)
    journalpagelink = models.CharField(max_length=200, null=True, blank=True)
    arxivlink = models.CharField(max_length=200, null=True, blank=True)
    titlelink = models.CharField(max_length=200, null=True, blank=True)
    bibref = models.CharField(max_length=200, null=True, blank=True)
    timescited = models.CharField(max_length=20, null=True, blank=True)

    authors = models.ManyToManyField(Person,through='Order')
    # authors = models.ManyToManyField(Person)    
    fromclass = models.ManyToManyField(Course, blank=True)

    image = models.FileField(upload_to=rename_files_paper,default="paper/blank.png",
                             help_text="Timestamp will automatically be added.")

    def __unicode__(self):
        return self.title

class Order(models.Model):
    author = models.ForeignKey(Person)
    paper = models.ForeignKey(Paper)
    order = models.IntegerField(default=0)
        
def rename_files_press(instance,filename):
    return datetime.now().strftime("press/%Y-%m-%d-%H-%M-{0}".format(filename))            
    
# press
# points to papers, projects, people
class Press(models.Model):
    title = models.CharField(max_length=500, default="UVM Researcher catapaults into fame.")
    url = models.CharField(max_length=2000, default="http://www.nytimes.com")
    author = models.CharField(max_length=200, null=True, blank=True,)
    date = models.DateTimeField('date published')
    description = models.CharField(max_length=2000, null=True, blank=True)
    favorite = models.CharField(max_length=10, null=True, blank=True,)
    imagelink = models.CharField(max_length=200, null=True, blank=True)
    organization = models.CharField(max_length=200, null=True, blank=True)
    papers = models.ManyToManyField(Paper, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    people = models.ManyToManyField(Person, blank=True)
    image = models.FileField(upload_to=rename_files_press,default="press/blank.png",
                             help_text="Timestamp will automatically be added.")

    def __unicode__(self):
        return self.title 













