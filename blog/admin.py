from turtle import update
from django.contrib import admin
from jmespath import search
#Models
from .models import Post

# Register your models here.
#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'desc', 'created')
    list_display_links = ('id', 'title')
    list_filter = ('created', 'updated')
    search_fields = ('title', 'desc')
    
    readonly_fields = ('created', 'updated')

