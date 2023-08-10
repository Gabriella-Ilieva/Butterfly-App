from datetime import date
import django_filters
from django import forms
from .models import Initiative, Categories, Groups, Regions


class InitiativeFilter(django_filters.FilterSet):
    category = django_filters.MultipleChoiceFilter(
        choices=Categories.choices(),
        widget=forms.CheckboxSelectMultiple,
    )

    suitable_for = django_filters.MultipleChoiceFilter(
        choices=Groups.choices(),
        widget=forms.CheckboxSelectMultiple,
    )

    region = django_filters.ChoiceFilter(
        choices=Regions.choices(),
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

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('expired', 'Expired'),
    )

    status = django_filters.ChoiceFilter(
        choices=STATUS_CHOICES,
        method='filter_by_status',
        label='Status',
    )

    def filter_by_status(self, queryset, name, value):
        today = date.today()

        if value == 'active':
            return queryset.filter(to_date__gte=today)
        elif value == 'expired':
            return queryset.filter(to_date__lt=today)

        return queryset

    class Meta:
        model = Initiative
        fields = ['category', 'region', 'suitable_for', 'from_date', 'to_date']

