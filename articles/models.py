from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from drafts.models import Draft, PublishedDraftManager
from comments.models import Comment


class Article(Draft):
    objects = models.Manager()
    published = PublishedDraftManager()
    comments = GenericRelation(Comment, related_query_name='article')
