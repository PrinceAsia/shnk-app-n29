from django.contrib.auth import get_user_model
from django.db import models

from app_shnk.models import SHNKDocumentsModel


# Create your models here.
class Comment(models.Model):
    comment_text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_likes = models.ManyToManyField(get_user_model(), related_name="comment_likes", blank=True)
    comment_dislikes = models.ManyToManyField(get_user_model(), related_name="comment_dislikes", blank=True)
    comment_reply = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True)
    comment_doc = models.ForeignKey(SHNKDocumentsModel, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.comment_text

    class Meta:
        ordering = ['comment_date']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comments'

# comment_text
# comment_author
# comment_time
# comment_doc
# comment_reply (optional)
# comment_likes (optional)
# comment_dislikes (optional)
# status (default=True)

