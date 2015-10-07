from django.contrib import admin

# Register your models here.
from cmplxsys.models import Person,Paper,Press,Funding,Project,Course,Order,Position

# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('website','strava') 

class OrderInline(admin.TabularInline):
    model = Order
    extra = 1

class PositionInline(admin.TabularInline):
    model = Position
    extra = 0

class PaperAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = (OrderInline,)
    filter_horizontal = ('authors','fromclass')

class PressAdmin(admin.ModelAdmin):
    filter_horizontal = ('papers','projects','people')

class FundingAdmin(admin.ModelAdmin):
    filter_horizontal = ('project',)

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('people',)

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('students','teachers')

class PersonAdmin(admin.ModelAdmin):
    inlines = (OrderInline,PositionInline,)    
    search_fields = ['fullname']

admin.site.register(Person,PersonAdmin)
admin.site.register(Paper,PaperAdmin)
admin.site.register(Press,PressAdmin)
admin.site.register(Funding,FundingAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Course,CourseAdmin)
