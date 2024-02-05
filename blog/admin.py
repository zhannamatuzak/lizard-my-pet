from django.contrib import admin
from .models import Lizard, Experience
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Lizard)
class LizardAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'description']
    summernote_fields = ('description', 'diet_list')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = ('pet_name', 'size', 'body', 'post', 'created_on')
    list_filter = ('user', 'post', 'created_on')
    search_fields = ('pet_name', 'size', 'body')
    actions = ['approve_comments']

    def approve_experiences(self, request, queryset):
        queryset.update(approved=True)
