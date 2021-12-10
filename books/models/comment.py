import logging

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from userprofile.models import UserProfile
from books.models import Book, Chapter

from utils.base_models import BaseTimeStampModel

logger = logging.getLogger(__name__.split('.')[0])


class Comment(BaseTimeStampModel):
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="%(class)s")
    content = models.TextField(null=True, blank=True)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.id


class Reply(BaseTimeStampModel):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    reply = models.TextField(null=True, blank=True)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.user.full_name

    @property
    def get_replies(self):
        return self.replies.all()
