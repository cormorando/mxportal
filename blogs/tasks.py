from __future__ import absolute_import, unicode_literals
from celery import task
from django.db.models import F
from blogs.models import Entry


@task(bind=True)
def increment_comments(self, pk):
    print('Request: {0!r}'.format(self.request))

    entry = Entry.objects.get(pk=pk)
    entry.comments_count = F('comments_count') + 1
    entry.save()
