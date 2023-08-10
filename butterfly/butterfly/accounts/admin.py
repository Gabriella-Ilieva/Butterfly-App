from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email')
    list_filter = ('username',)
    search_fields = ('username', 'first_name', 'last_name')
    search_help_text = 'Search by Username, First name or Last name'
