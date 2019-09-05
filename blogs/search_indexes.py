from datetime import datetime
from haystack import indexes
from blogs.models import Entry


class EntryIndex(indexes.SearchIndex, indexes.Indexable):
        text = indexes.EdgeNgramField(document=True, use_template=True)
        title = indexes.CharField(model_attr='title')
        body = indexes.CharField(model_attr='body')
        pub_date = indexes.DateTimeField(model_attr='pub_date')

        def get_model(self):
            return Entry

        def index_queryset(self, using=None):
            return self.get_model().objects.filter(pub_date__lte=datetime.now())
