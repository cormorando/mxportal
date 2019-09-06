from datetime import datetime
from django.db import models


class PublishedDraftManager(models.Manager):
    def get_queryset(self):
        return super(PublishedDraftManager, self).get_queryset().filter(pub_date__lte=datetime.now())


class Draft(models.Model):
    title = models.CharField(max_length=200, default='')
    body = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(blank=True)
    comments_count = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        abstract = True
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
