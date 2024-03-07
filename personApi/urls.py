from django.urls import path
from personApi.views import PersonGetUpdateDeleteView, PersonListView

urlpatterns = [
    path('persons/', PersonListView.as_view(), name='person-list'),
    path('persons/<int:pk>/', PersonGetUpdateDeleteView.as_view(), name='person-detail'),
]