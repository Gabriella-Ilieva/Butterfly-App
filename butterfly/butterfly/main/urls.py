from django.urls import path

from butterfly.main.views import index, comment_functionality

urlpatterns = [
    path('', index, name="index"),
    path('comment/<int:initiative_pk>', comment_functionality, name="comment"),
]
