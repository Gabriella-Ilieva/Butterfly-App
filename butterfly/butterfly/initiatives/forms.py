from django import forms

from butterfly.initiatives.models import Initiative


class CreateInitiativeForm(forms.ModelForm):
    class Meta:
        model = Initiative
        exclude = ['date_of_publication', 'user']

        widgets = {
            'from_date': forms.DateInput(
                attrs={
                    'placeholder': 'When the initiative starts?',
                    'type': 'date'
                }
            ),
            'to_date': forms.DateInput(
                attrs={
                    'placeholder': 'When the initiative ends?',
                    'type': 'date'
                }
            ),
        }


class EditInitiativeForm(forms.ModelForm):
    class Meta:
        model = Initiative
        exclude = ['date_of_publication', 'user']

