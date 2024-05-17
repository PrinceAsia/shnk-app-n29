from django_filters.rest_framework import FilterSet

from app_comments.models import Comment


class CommentDocFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'comment_doc': ['exact'],
        }