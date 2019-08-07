from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blogs.models import Entry


class EntryListView(ListView):

    model = Entry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class EntryDetailView(DetailView):

    model = Entry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
