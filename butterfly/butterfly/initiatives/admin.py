from django.contrib import admin
from .models import Initiative, Participation


@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'from_date', 'to_date', 'user')

    list_filter = (
        'category',
        'suitable_for',
        'region',
        'to_date',
        ('user', admin.RelatedOnlyFieldListFilter)
    )
    search_fields = ('title',)
    search_help_text = 'Search by Title'


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('show_username', 'show_initiative_title')
    list_filter = (('user', admin.RelatedOnlyFieldListFilter),)
    search_fields = ('to_initiative__title', )
    search_help_text = 'Search by Initiative Title'

    def show_initiative_title(self, obj):
        return obj.to_initiative.title
    show_initiative_title.short_description = 'Inititative Title'

    def show_username(self, obj):
        return obj.user.username
    show_username.short_description = 'User'

    show_initiative_title.admin_order_field = 'to_initiative__title'
    show_username.admin_order_field = 'user__username'
