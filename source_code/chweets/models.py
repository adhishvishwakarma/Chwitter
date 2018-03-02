from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings


class Chweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=False)
    content = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content)

