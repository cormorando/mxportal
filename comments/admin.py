from django.contrib import admin
from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'created',)

admin.site.register(Comment, CommentAdmin)
