from django.urls import path

from butterfly.initiatives.views import all_initiatives, CreateInitiativeView, initiative_details, edit_initiative, \
    DeleteInitiativeView

urlpatterns = [
    path('', all_initiatives, name='all initiatives'),
    path('create/', CreateInitiativeView.as_view(), name='add initiative'),
    path('details/<int:pk>/', initiative_details, name='details initiative'),
    path('edit/<int:pk>/', edit_initiative, name='edit initiative'),
    path('delete/<int:pk>/', DeleteInitiativeView.as_view(), name='delete initiative')
]
