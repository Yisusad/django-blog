from django.contrib import admin
from jmespath import search

#Models
from .models import Project

# Register your models here.
#admin.site.register(Project)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'created')
    list_editable = ('title',)
    list_filter = ('title', 'created', 'updated')
    search_fields = ('title',)
    
        
