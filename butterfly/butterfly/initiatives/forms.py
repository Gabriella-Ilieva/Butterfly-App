from django import forms

from butterfly.initiatives.models import Initiative


class CreateInitiativeForm(forms.ModelForm):
    class Meta:
        model = Initiative
        exclude = ['date_of_publication', 'user']


class EditInitiativeForm(forms.ModelForm):
    class Meta:
        model = Initiative
        exclude = ['date_of_publication', 'user']
