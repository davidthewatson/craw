import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField


class WebPage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.TextField(unique=True)
    html = models.TextField()
    links = ArrayField(models.TextField())
    title = models.TextField()

    class Meta:
        managed = True
