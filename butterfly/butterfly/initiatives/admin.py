from django.contrib import admin
from .models import Initiative, Participation


@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    pass

