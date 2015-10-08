from cmplxsys.models import Person,Paper,Funding,Press,Project,Course,Position
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields

class BasicPersonResource(ModelResource):
    # positions = fields.ToManyField('cmplxsys.models.position','position_set',full=True)
    positions = fields.ToManyField('cmplxsys.api.BasicPositionResource','position_set',full=True)
    class Meta:
        # queryset = Person.objects.all().order_by('core_team_order')
        queryset = Person.objects.all()
        resource_name = 'personsimple'
        filtering = {
            'uname': ALL,
            'core_team': ALL,
            'associated_faculty': ALL,
            'alumni': ALL,
            'positions': ALL,
        }
        ordering = {
            'uname': ALL,
            'core_team_order': ALL,
            'positions': ALL,
        }

class BasicPositionResource(ModelResource):
    class Meta:
        queryset = Position.objects.all()
        resource_name = 'position'
        filtering = {
            'title': ALL,
            }

class PersonResource(ModelResource):
    # the person resource always gets their papers
    papers = fields.ManyToManyField('cmplxsys.api.BasicPaperResource','paper_set',full=True)
    # this works!! but only if the bundle is not empty
    # papers = fields.ManyToManyField('cmplxsys.api.BasicPaperResource',lambda bundle: bundle.obj.paper_set.all().order_by('-year'),full=True)

    # press = fields.ManyToManyField('cmplxsys.api.BasicPressResource',lambda bundle: Press.objects.all().order_by('-date'),full=True)
    press = fields.ManyToManyField('cmplxsys.api.BasicPressResource','press_set',full=True)
    # press = fields.ManyToManyField('cmplxsys.api.BasicPressResource',lambda bundle: bundle.obj.press_set.all().order_by('-date'),full=True)
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
        ordering = {
            'year': ALL,
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




