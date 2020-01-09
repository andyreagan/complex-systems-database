from django.db import models
from datetime import datetime,timedelta
from subprocess import call
# from scholar import *
import re

def rename_files_person(instance,filename):
    return datetime.now().strftime("people/%Y-%m-%d-%H-%M-{0}".format(filename))

# Create your models here.
# a model for the people
# pointed to by courses (twice), papers, projects, press, funding
# which is everything else
class Person(models.Model):
    # username
    uname = models.CharField(max_length=20,help_text="This is the username, used in links on the site. Make it a full name (because we can), i.e. Andy Reagan should be andyreagan, not areagan. A-Za-z characters allowed (for links sake).")
    # eventually can build a model for affiliations (VACC, UVM, CSYS, CS, MATH, etc)
    # but bigger fish to fry right now
    institution = models.CharField(max_length=200, default="University of Vermont",
                                   help_text="Ex: UVM, MITRE, ...")
    affiliation0 = models.CharField(max_length=200, default="Department of Mathematics and Statistics",
                                    null=True, blank=True,)
    role0 = models.CharField(max_length=200, default="Professor")
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
    fullname = models.CharField(max_length=200,help_text="This is the display name. Shown on headings for lists of people, and the personal page (and if following first,middle,last are blank, used for paper author name.")
    # split up name is optional, for now
    first = models.CharField(max_length=200, null=True, blank=True, default="",help_text="These first, middle, last, are for building the bibtex entry and display paper author lists.")
    middle = models.CharField(max_length=200, null=True, blank=True, default="",help_text="If an abbreviation, have the dot here.")
    last = models.CharField(max_length=200, null=True, blank=True, default="")
    sur = models.CharField(max_length=200, null=True, blank=True, default="")
    webpage = models.CharField(max_length=200, null=True, blank=True, default="",
                               help_text="Full URL of person webpage.")
    linkedin = models.CharField(max_length=200, null=True, blank=True, default="",
                               help_text="https://www.linkedin.com/_________")
    twitter = models.CharField(max_length=200, null=True, blank=True, default="",
                               help_text="Just the username.")
    strava = models.CharField(max_length=200, null=True, blank=True, default="",
                               help_text="https://www.strava.com/athletes/_________")
    facebook = models.CharField(max_length=200, null=True, blank=True, default="")
    youtube = models.CharField(max_length=200, null=True, blank=True, default="",
                               help_text="https://www.youtube.com/channel/________")
    vine = models.CharField(max_length=200, null=True, blank=True, default="")
    instagram = models.CharField(max_length=200, null=True, blank=True, default="")
    scholar = models.CharField(max_length=200, null=True, blank=True, default="")
    github = models.CharField(max_length=200, null=True, blank=True, default="",
                              help_text="Just the username.")
    bitbucket = models.CharField(max_length=200, null=True, blank=True, default="")
    stackoverflow = models.CharField(max_length=200, null=True, blank=True, default="")
    plus = models.CharField(max_length=200, null=True, blank=True, default="")
    pinterest = models.CharField(max_length=200, null=True, blank=True, default="")
    arxiv = models.CharField(max_length=200, null=True, blank=True, default="",
                             help_text="http://arxiv.org/__________")
    researchgate = models.CharField(max_length=200, null=True, blank=True, default="",
                             help_text="https://www.researchgate.net/profile/_________")
    orcid = models.CharField(max_length=19, null=True, blank=True, default="",
                             help_text="Please enter the full number (with the dashes): http://orcid.org/____-____-____-____")
    image = models.FileField(upload_to=rename_files_person,default="people/blank.png",
                             help_text="Timestamp will automatically be added and will automatically convert to grayscale.")
    collaborator = models.BooleanField(default=False,help_text="If they don't work at/go to UVM.")
    alumni = models.BooleanField(default=False,help_text="If they used to go here.")
    current_student = models.BooleanField(default=False,help_text="If they currently go here.")
    post_doc = models.BooleanField(default=False,help_text="Currently post doctoral scholar.")
    position_desc = models.CharField(max_length=400,null=True, blank=True, default="",help_text="Current position, or former degree awarded for alumni. For current, set either PD, PhD, MS, UG, CERT.")
    core_team = models.BooleanField(default=False,help_text="Will show up on the core team page.")
    core_team_order = models.IntegerField(default=0,help_text="Order to sort if core_team=True.")
    associated_faculty = models.BooleanField(default=False,help_text="Will show up on the associated faculty page.")

    def __unicode__(self):
        return self.fullname

    # class Meta:
    #     ordering = ('order__order',)
        # order_with_respect_to = 'order__order'

    def save(self, *args, **kwargs):
        # return datetime.now().strftime("people/%Y-%m-%d-%H-%M-{0}".format(filename))
        command = datetime.now().strftime("convert -geometry 163x -colorspace Gray {0} {0}".format(self.image._get_path()))
        # do not grayscale the image, because we can do this in CSS
        # call(command,shell=True)
        # we also don't need to make it square, since we can handle that in CSS too
        # (also, make it a circle in CSS)
        super(Person, self).save(*args, **kwargs)

class Position(models.Model):
    TITLE_CHOICES = (
        ('PD', 'Post Doctoral Fellow'),
        ('PHD', 'PhD Student'),
        ('MS', 'Masters Student'),
        ('UG', 'Undergraduate Student'),
        ('CERT', 'Certificate of Study in Complex Systems'),
        )

    title = models.CharField(max_length=4,
                             choices=TITLE_CHOICES,
                             default='PHD')
    startyear = models.CharField(max_length=10,default='2015')
    endyear = models.CharField(max_length=10,default='Current')
    person = models.ForeignKey(Person)

    def __unicode__(self):
        return self.title

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
    imagelink = models.URLField(max_length=200, null=True, blank=True)

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
    journal = models.CharField(max_length=200, null=True, blank=True,default="Preprint",help_text="Name of the journal. Leave \"Preprint\" for preprints")
    volume = models.CharField(max_length=200, null=True, blank=True)
    issue = models.CharField(max_length=200, null=True, blank=True,help_text="Will be exported as \"number\" in bibtex. I.e. the 1 in \"EPJ Data Science, 5(1), 237-239.\"")
    pages = models.CharField(max_length=200, null=True, blank=True)
    year = models.IntegerField(default=1950,help_text="Date to be used for formatting the citation.")
    sort_date = models.DateTimeField(help_text="Date to be used for sorting the paper in lists on the site.")
    googlescholarlink = models.URLField(max_length=200, null=True, blank=True)
    preprintlink = models.URLField(max_length=200, null=True, blank=True, help_text="This will be the url to which PDF is linked.")
    supplementarylink = models.URLField(max_length=200, null=True, blank=True)
    onlineappendices = models.URLField(max_length=200, null=True, blank=True)
    journalpagelink = models.URLField(max_length=200, null=True, blank=True)
    arxivlink = models.URLField(max_length=200, null=True, blank=True)
    titlelink = models.URLField(max_length=200, null=True, blank=True, help_text="Link that will download on click of the title.")
    bibref = models.CharField(max_length=200, null=True, blank=True,help_text="This will be generated automatically as well, don't both filling out unless you don't want the Google Scholar format, e.g. \"dodds2016positivity\".")
    timescited = models.CharField(max_length=20, null=True, blank=True,help_text="We'll automatically try to fill this on save using google scholar (and set the cluster_id below).")
    google_scholar_cluster_id = models.CharField(max_length=40, null=True, blank=True)
    google_scholar_result_found = models.BooleanField(default=False)
    google_scholar_most_recent_date = models.DateTimeField(null=True, blank=True)
    google_scholar_raw_result = models.TextField(null=True, blank=True)
    DOI = models.CharField(max_length=200, null=True, blank=True)
    PMID= models.CharField(max_length=200, null=True, blank=True)
    ISSN = models.CharField(max_length=200, null=True, blank=True)
    altmetric_id = models.CharField(max_length=100, null=True, blank=True)
    author_list_sorted = models.BooleanField(default=False,help_text="Set this to true when the author list is ordered. Will hide the warning on the paper page.")
    #storylab = models.BooleanField(default=False)
    authors = models.ManyToManyField(Person,through='Order')
    # authors = models.ManyToManyField(Person)    
    fromclass = models.ManyToManyField(Course, blank=True)

    image = models.FileField(upload_to=rename_files_paper,default="papers/blank.png",
                             help_text="Timestamp will automatically be added.")

    class Meta:
        ordering = ['-sort_date']
        
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Paper, self).save(*args, **kwargs)
        # if self.bibref == "" or not self.bibref:
        # automatically regenerate...why not
        if True:
            def get_first_noun(title):
                non_nouns = ["the","of"]
                i = 0
                while title.split(" ")[i].lower() in non_nouns:
                    i+=1
                # this extracts only the a-z characters
                # return title.split(" ")[i].lower().replace("'","")
                # weak, do better
                # return "".join(re.split("[^a-z]*", title.split(" ")[i].lower())
                # this also works, a bit cleaner I think
                return re.sub(r"[^a-z]+", "", title.split(" ")[i].lower())
            if len(self.authors.all()) == 0:
                print(self.title," has no authors")
                firstauthor = "unknown"
            else:
                firstauthor = self.authors.all()[0].last.lower()
            self.bibref = firstauthor + str(self.year) + get_first_noun(self.title)
            super(Paper, self).save(*args, **kwargs)

        # querier = ScholarQuerier()
        # settings = ScholarSettings()
        # querier.apply_settings(settings)
        # if self.google_scholar_cluster_id:
        #     query = ClusterScholarQuery(cluster=self.google_scholar_cluster_id)
        # else:
        #     query = SearchScholarQuery()
        #     if len(self.authors.all().order_by('order')) > 0:
        #         query.set_author(self.authors.all().order_by('order')[0].fullname)
        #     query.set_phrase(self.title)
        #     # tell it to look only for title
        #     # query.set_scope(True)
        #     query.set_num_page_results(1)

        # if self.google_scholar_most_recent_date < (datetime.now()-timedelta(days=1)):
        if False:
            # look at this query we've constructed
            # print(query)
            self.google_scholar_most_recent_date = datetime.now()
            querier.send_query(query)
            # look at this querier object after hitting google
            # print(querier)
            print(len(querier.articles))
            if len(querier.articles) > 0:
                self.google_scholar_result_found = True
                self.google_scholar_raw_result = str(querier.articles[0].attrs)
                # print(querier.articles[0].attrs)
                if self.year == 1950 and querier.articles[0].attrs['year'][0]:
                    self.year = int(querier.articles[0].attrs['year'][0])
                    # print("updating year")
                self.timescited = querier.articles[0].attrs['num_citations'][0]
                # print("updated citation count")
                if querier.articles[0].attrs['cluster_id'][0]:
                    self.google_scholar_cluster_id = querier.articles[0].attrs['cluster_id'][0]
                #     print("updated cluster id")
                # print("updated, saving...")
                super(Paper, self).save(*args, **kwargs)
            else:
                # print("no result, saving...")
                super(Paper, self).save(*args, **kwargs)

class Order(models.Model):
    author = models.ForeignKey(Person)
    paper = models.ForeignKey(Paper)
    order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['order']
        
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
    favorite = models.IntegerField(default=0, null=True, blank=True,help_text="An integer than can be used to sort the press by.")
    imagelink = models.URLField(max_length=200, null=True, blank=True,help_text="Not used (better to save the image in the database using \"image\" field at the bottom)")
    organization = models.CharField(max_length=200, null=True, blank=True,help_text="e.g. New York Times")
    papers = models.ManyToManyField(Paper, blank=True,help_text="Will show up with paper, and in people's \"all press\" feed and/or \"first author\" feed.")
    projects = models.ManyToManyField(Project, blank=True,help_text="Will show up for the project, and for a person's press_project feed.")
    people = models.ManyToManyField(Person, blank=True, help_text="Favorited by these people (will show up the \"favorited\" feed.")
    image = models.FileField(upload_to=rename_files_press,default="press/blank.png",
                             help_text="Timestamp will automatically be added.")

    def __unicode__(self):
        return self.title 

    class Meta:
        ordering = ['-date']

class Event(models.Model):
    title = models.CharField(max_length=500, default="Life Changing Event")
    start_date = models.DateTimeField('Event Start Date')
    end_date = models.DateTimeField('Event End Date')
    location = models.CharField(max_length=500, default="Burlington, Vermont")
    description = models.TextField(default="There are none.",help_text="LaTeX format")
    organizer_name = models.CharField(max_length=500,default="Roboctopus")
    organizer_email = models.EmailField(max_length=500, null=True, blank=True)
    event_page = models.URLField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return self.title
