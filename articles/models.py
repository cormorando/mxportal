from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from drafts.models import Draft, DraftManager
from comments.models import Comment


class Article(Draft):
    published = DraftManager()
    comments = GenericRelation(Comment, related_query_name='article')
