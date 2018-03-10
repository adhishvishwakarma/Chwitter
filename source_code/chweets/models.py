from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings
from django.utils import timezone


class ChweetManager(models.Manager):
    def rechweet(self, user, parent_obj):
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent = parent_obj
        qs = self.get_queryset().filter(
            user=user, parent=og_parent
        ).filter(
            timestamp__year=timezone.now().year,
            timestamp__month=timezone.now().month,
            timestamp__day=timezone.now().day,
        )
        if qs.exists():
            return None
        obj = self.model(
            parent=og_parent,
            user=user,
            content=parent_obj.content,
        )
        obj.save()
        return obj


class Chweet(models.Model):
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=False)
    content = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ChweetManager()

    def __str__(self):
        return str(self.content)

