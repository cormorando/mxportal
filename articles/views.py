from django.shortcuts import render
from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleListView(ListView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ArticleDetailView(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
