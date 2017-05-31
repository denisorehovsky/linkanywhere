import uuid

from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from behaviors.behaviors import Timestamped

from linkanywhere.apps.likes.models import Like


class Link(Timestamped, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='links'
    )
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()
    likes = GenericRelation(Like)
    category = models.ForeignKey(
        'categories.Category', on_delete=models.CASCADE, related_name='links'
    )
    tags = models.ManyToManyField(
        'tags.Tag', related_name='links'
    )

    def __str__(self):
        return '{0}: {1}'.format(self.title, self.url)

    @property
    def total_likes(self):
        return self.likes.count()
