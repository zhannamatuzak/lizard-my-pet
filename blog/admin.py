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


admin.site.register(Experience)