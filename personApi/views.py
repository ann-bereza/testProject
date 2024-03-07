import csv

from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.views import FilterView
from rest_framework.decorators import action, renderer_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from rest_framework.settings import api_settings

from .filters import PersonFilter
from .models import Person
from .serializer import PersonSerializer
from rest_framework_csv.renderers import CSVRenderer


# class PersonListView(FilterView, ListCreateAPIView):
#     template_name = 'filters.html'
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#     filterset_class = PersonFilter

# class PersonListView1(ListCreateAPIView):
#     model = Person
#     serializer_class = PersonSerializer
#
#     def get_queryset(self):
#         category = self.request.query_params.get('category')
#         gender = self.request.query_params.get('gender')
#         objects = Person.objects.all()
#         if category:
#             objects = objects.filter(category=category)
#         if gender:
#             objects = objects.filter(gender=gender)
#         return objects
#
#


class PersonListView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'gender', 'birth_date']


class PersonGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

