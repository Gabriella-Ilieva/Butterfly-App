from django.contrib import admin

from butterfly.main.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_time_of_publication', 'show_initiative_title')
    list_filter = (
        ('user', admin.RelatedOnlyFieldListFilter),)
    search_fields = ('to_initiative__title',)
    search_help_text = 'Search by Initiative Title'

    def show_initiative_title(self, obj):
        return obj.to_initiative.title
    show_initiative_title.short_description = 'Initiative Title'