from django.urls import path, include

from butterfly.stories.views import CreateStoryView, DeleteStoryView, show_all_stories, story_details, edit_story

urlpatterns = (
    path('', show_all_stories, name='all stories'),
    path('create/', CreateStoryView.as_view(), name='add story'),
    path('details/<int:pk>/', story_details, name='details story'),
    path('edit/<int:pk>/', edit_story, name='edit story'),
    path('delete/<int:pk>/', DeleteStoryView.as_view(), name='delete story')
)