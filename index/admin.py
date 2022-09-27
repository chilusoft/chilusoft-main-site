from django.contrib import admin

# Register your models here.
from .models import ProjectCategory, Project, User

# make a model Admin class
@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_added', 'date_updated')
    list_filter = ('name', 'date_added', 'date_updated')
    search_fields = ('name', 'hyperlink', 'date_added', 'date_updated')
    ordering = ('name', 'date_added', 'date_updated')
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'date_added')
    list_filter = ('name', 'category', 'date_added')
    search_fields = ('name', 'category', 'date_added')
    ordering = ('name', 'category', 'date_added')
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'access_level', 'date_joined')
    list_filter = ('username', 'access_level', 'date_joined')
    search_fields = ('username', 'access_level', 'date_joined')
    ordering = ('username', 'access_level', 'date_joined')