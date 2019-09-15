from datetime import datetime
from django.db import models
from meta.models import ModelMeta
from rake_nltk import Rake


class PublishedDraftManager(models.Manager):
    def get_queryset(self):
        return super(PublishedDraftManager, self).get_queryset().filter(pub_date__lte=datetime.now())


class Draft(ModelMeta, models.Model):
    title = models.CharField(max_length=200, default='')
    body = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(blank=True)
    comments_count = models.PositiveIntegerField(default=0, editable=False)

    _metadata = {
        'use_title_tag': 'true',
        'title': 'title',
        'description': 'get_meta_description',
        'keywords': 'get_meta_keywords',
    }

    class Meta:
        abstract = True
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def get_meta_description(self):
        return self.body[:155]

    def get_meta_keywords(self):
        r = Rake()
        r.extract_keywords_from_text(self.body)

        return r.get_ranked_phrases()[:10]
