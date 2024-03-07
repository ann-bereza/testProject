import datetime

from django_filters import rest_framework as filters

from .models import Person


class PersonFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category', lookup_expr='exact')
    gender = filters.CharFilter(field_name='gender', lookup_expr='exact')
    birth_date = filters.DateFilter(field_name='birth_date')

    min_age = filters.NumberFilter(field_name='age', method='filter_min_age')
    max_age = filters.NumberFilter(field_name='age', method='filter_max_age')

    class Meta:
        model = Person
        fields = ['category', 'gender', 'birth_date', 'min_age', 'max_age']

    def filter_min_age(self, queryset, name, value):
        today = datetime.date.today()
        birth_year = today.year - value
        return queryset.filter(birth_date__lte=datetime.date(birth_year, today.month, today.day))

    def filter_max_age(self, queryset, name, value):
        today = datetime.date.today()
        birth_year = today.year - value - 1
        return queryset.filter(birth_date__gte=datetime.date(birth_year, today.month, today.day))
