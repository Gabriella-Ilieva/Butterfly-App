from django.urls import path

from butterfly.main.views import index

urlpatterns = [
    path('', index, name="index"),
]