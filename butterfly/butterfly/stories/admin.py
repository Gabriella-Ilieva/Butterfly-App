from django.contrib import admin
from .models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_of_publication')
    list_filter = (('user', admin.RelatedOnlyFieldListFilter),)
    search_fields = ('title',)
    search_help_text = 'Search by Story Title'
