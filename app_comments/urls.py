from django.urls import path
from rest_framework import routers

from .views import CommentsViewSet, set_reaction_to_comment

router = routers.DefaultRouter()

router.register('', CommentsViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('reaction/<str:reaction_type>/<int:comment_id>/', set_reaction_to_comment, name='set_reaction_to_comment'),
]
