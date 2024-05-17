# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from app_comments.filters import CommentDocFilter
from app_comments.models import Comment
from app_comments.permissions import IsOwnerOrReadOnly
from app_comments.serializers import CommentSerializer


# Create your views here.
class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentDocFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(Comment.objects.filter(status=True))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author == self.request.user or request.user.is_superuser:
            instance.status = False
            instance.save()
            return Response(
                data={'message': 'Comment successfully deleted.'},
                status=status.HTTP_204_NO_CONTENT
            )
        return Response(
            data={'message': 'You are not allowed to delete this comment.'},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


@api_view(['POST'])
def set_reaction_to_comment(request, comment_id, reaction_type):
    if request.user.is_authenticated:
        try:
            comment = Comment.objects.get(pk=comment_id)
            if reaction_type == 'like':
                if request.user in comment.comment_likes.all():
                    comment.comment_likes.remove(request.user)
                    return Response(
                        data={'message': 'Like canceled.'},
                        status=status.HTTP_200_OK
                    )
                else:
                    if request.user in comment.comment_dislikes.all():
                        comment.comment_dislikes.remove(request.user)
                    comment.comment_likes.add(request.user)
                    return Response(
                        data={'message': 'Liked.'},
                        status=status.HTTP_200_OK
                    )
            elif reaction_type == 'dislike':
                if request.user in comment.comment_dislikes.all():
                    comment.comment_dislikes.remove(request.user)
                    return Response(
                        data={'message': 'Dislike canceled.'},
                        status=status.HTTP_200_OK
                    )
                else:
                    if request.user in comment.comment_likes.all():
                        comment.comment_likes.remove(request.user)
                    comment.comment_dislikes.add(request.user)
                    return Response(
                        data={'message': 'Disliked.'},
                        status=status.HTTP_200_OK
                    )
            else:
                return Response(
                    data={'message': 'Unknown reaction type.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Comment.DoesNotExist:
            return Response(
                data={'message': 'Comment does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

    else:
        return Response(
            data={'message': 'You could not react to this comment without authentication.'},
            status=status.HTTP_401_UNAUTHORIZED
        )
