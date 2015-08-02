from cmplxsys.models import Person,Paper,Funding,Press,Project,Course
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields

class BasicPersonResource(ModelResource):
    class Meta:
        queryset = Person.objects.all()
        resource_name = 'personsimple'
        filtering = {
            'uname': ALL,
        }
        ordering = {
            'uname': ALL,
            # 'order': ALL,
        }

class PersonResource(ModelResource):
    # the person resource always gets their papers
    papers = fields.ManyToManyField('cmplxsys.api.BasicPaperResource','paper_set',full=True)
    # press = fields.ManyToManyField('cmplxsys.api.BasicPressResource',lambda bundle: Press.objects.all().order_by('-date'),full=True)
    press = fields.ManyToManyField('cmplxsys.api.BasicPressResource','press_set',full=True)    
    # .order_by('-date')
    funding = fields.ManyToManyField('cmplxsys.api.BasicFundingResource','funding_set',full=True)
    projects = fields.ManyToManyField('cmplxsys.api.BasicProjectResource','project_set',full=True)

    classes_taught = fields.ManyToManyField('cmplxsys.api.BasicCourseResource','courses_taken',full=True)
    classes_taken = fields.ManyToManyField('cmplxsys.api.BasicCourseResource','courses_taught',full=True)
    
    class Meta:
        queryset = Person.objects.all()
        resource_name = 'person'
        filtering = {
            'uname': ALL,
            'papers': ALL,
        }

class BasicPaperResource(ModelResource):
    class Meta:
        queryset = Paper.objects.all().order_by('-year')
        resource_name = 'paper'
        filtering = {
            'title': ALL,
            'id': ALL,
            'author': ALL,
        }

class PaperResource(ModelResource):
    # the paper resource always gets the authors
    # author = fields.ToManyField('cmplxsys.api.BasicPersonResource','authors',full=True)
    # author = fields.ManyToManyField('cmplxsys.api.BasicPersonResource',lambda bundle: Person.objects.filter().order_by('order'),full=True)
    author = fields.ManyToManyField('cmplxsys.api.BasicPersonResource',lambda bundle: bundle.obj.authors.all().order_by('order__order'),full=True)
    
    # and the press
    press = fields.ManyToManyField('cmplxsys.api.BasicPressResource','press_set',full=True)

    class Meta:
        queryset = Paper.objects.all()
        resource_name = 'paper'
        filtering = {
            'title': ALL,
            'id': ALL,
            'author': ALL,
            'press': ALL,
        }
        ordering = {
            'author': ALL,
        }

class BasicFundingResource(ModelResource):
    class Meta:
        queryset = Funding.objects.all()
        resource_name = 'funding'
        filtering = {
            'source': ALL,
        }

class BasicProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
        filtering = {
            'title': ALL,
        }

class BasicPressResource(ModelResource):
    class Meta:
        queryset = Press.objects.all().order_by('-date')
        resource_name = 'press'
        filtering = {
            'date': ALL,
        }
        ordering = {
            'date': ALL,
        }

class RecentPressResource(ModelResource):
    class Meta:
        queryset = Press.objects.all().order_by('-date')
        resource_name = 'recentpress'
        limit = 50
        filtering = {
            'date': ALL,
        }

class BasicCourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'course'
        filtering = {
            'date': ALL,
        }            




