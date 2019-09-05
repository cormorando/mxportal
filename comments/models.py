from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Comment(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def url(instance):
        return instance.content_object.url()
