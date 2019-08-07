from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from drafts.models import Draft, PublishedDraftManager
from comments.models import Comment


class Entry(Draft):
    objects = models.Manager()
    published = PublishedDraftManager()
    comments = GenericRelation(Comment, related_query_name='entry')

    class Meta:
        verbose_name_plural = 'entries'
