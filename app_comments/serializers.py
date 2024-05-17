from rest_framework import serializers

from app_comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # exclude = ['status']
        extra_kwargs = {
            'status': {'read_only': True},
            'comment_likes': {'read_only': True},
            'comment_dislikes': {'read_only': True},
            'author': {'read_only': True},
        }
