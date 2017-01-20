from django.contrib import admin

# Register your models here.
from cmplxsys.models import *

# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('website','strava')

from suit.admin import SortableModelAdmin

# class OrderInline(SortableModelAdmin):
#     fk_name = 'paper'
#     model = Order
#     sortable = 'order'
#     extra = 0

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0

# class AuthorInline(admin.TabularInline):
#     model = Person
#     extra = 0

class PositionInline(admin.TabularInline):
    model = Position
    extra = 0

class PaperAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = (OrderInline,)
    # filter_horizontal = ('authors','fromclass')
    # trying to play nice with django-suit
    # fieldsets = [
    #         (None, {
    #             'classes': (),
    #             'fields': [],}),
    #         ('Orders', {
    #             'classes': (),
    #             'fields': [],}),
    #     ]
        
class PressAdmin(admin.ModelAdmin):
    filter_horizontal = ('papers','projects','people')
    search_fields = ['title']
    list_display = ('date','title','organization','url',)
    list_display_links = ('url',)
    # list_editable = (,)

class FundingAdmin(admin.ModelAdmin):
    filter_horizontal = ('project',)

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('people',)

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('students','teachers')

class PersonAdmin(admin.ModelAdmin):
    # inlines = (OrderInline,PositionInline,)
    search_fields = ['fullname']

admin.site.register(Person,PersonAdmin)
admin.site.register(Paper,PaperAdmin)
admin.site.register(Press,PressAdmin)
admin.site.register(Funding,FundingAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Course,CourseAdmin)
# admin.site.register(Order)
# admin.site.register(Position)
