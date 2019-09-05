from django.views.generic import TemplateView
from haystack.generic_views import SearchView
from haystack.forms import SearchForm


class HomeView(TemplateView):
    template_name = 'home.html'


class HighlightedSearchView(SearchView):

    def get_queryset(self):
        queryset = super(HighlightedSearchView, self).get_queryset()

        return queryset.highlight()

    def get_context_data(self, *args, **kwargs):
        context = super(HighlightedSearchView, self).get_context_data(*args, **kwargs)

        return context
