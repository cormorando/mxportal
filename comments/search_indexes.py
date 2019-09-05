from datetime import datetime
from haystack import indexes
from comments.models import Comment


class EntryIndex(indexes.SearchIndex, indexes.Indexable):
        text = indexes.EdgeNgramField(document=True, use_template=True)
        body = indexes.CharField(model_attr='body')
        created = indexes.DateTimeField(model_attr='created')

        def get_model(self):
            return Comment

        def index_queryset(self, using=None):
            return self.get_model().objects.all()
