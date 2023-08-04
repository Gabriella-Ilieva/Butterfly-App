import django_filters
from django import forms

from .models import Initiative


class InitiativeFilter(django_filters.FilterSet):
    category = django_filters.MultipleChoiceFilter(
        choices=Initiative.CATEGORIES,
        widget=forms.CheckboxSelectMultiple,
    )

    suitable_for = django_filters.MultipleChoiceFilter(
        choices=Initiative.GROUPS,
        widget=forms.CheckboxSelectMultiple,
    )

    region = django_filters.ChoiceFilter(
        choices=Initiative.REGIONS,
        widget=forms.Select,
    )

    from_date = django_filters.DateFilter(
        field_name='from_date',
        lookup_expr='gte',
        widget=forms.DateInput(
            attrs={'type': 'date'}
        ))

    to_date = django_filters.DateFilter(
        field_name='to_date',
        lookup_expr='lte',
        widget=forms.DateInput(
            attrs={'type': 'date'}
        ))

    class Meta:
        model = Initiative
        fields = ['category', 'region', 'suitable_for', 'from_date', 'to_date']

