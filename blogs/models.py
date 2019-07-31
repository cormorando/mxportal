from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from drafts.models import Draft, DraftManager
from comments.models import Comment


class Entry(Draft):
    published = DraftManager()
    comments = GenericRelation(Comment, related_query_name='entry')

    class Meta:
        verbose_name_plural = 'entries'
