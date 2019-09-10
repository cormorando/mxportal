import json
from django.views.generic import TemplateView
from django.http import HttpResponse
from haystack.generic_views import SearchView
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet


class HomeView(TemplateView):
    template_name = 'home.html'


class HighlightedSearchView(SearchView):

    def get_queryset(self):
        queryset = super(HighlightedSearchView, self).get_queryset()

        return queryset.highlight()

    def get_context_data(self, *args, **kwargs):
        context = super(HighlightedSearchView, self).get_context_data(*args, **kwargs)

        return context

    def autocomplete(request):
        if request.is_ajax():
            sqs = SearchQuerySet().autocomplete(text=request.GET.get('term', ''))[:5]
            suggestions = [result.title if result.title else result.body for result in sqs]

        data = json.dumps(suggestions or ['No suggestions'])

        return HttpResponse(data, 'application/json')
