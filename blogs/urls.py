from django.urls import path

from blogs.views import EntryListView, EntryDetailView

urlpatterns = [
    path('', EntryListView.as_view(), name='entry-list'),
    path('<int:pk>/', EntryDetailView.as_view(), name='entry-detail'),
]
