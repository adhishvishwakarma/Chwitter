from django.db import models
from chweets.models import Chweet


class HashTag(models.Model):
    tag = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag

    def get_chweets(self):
        return Chweet.objects.filter(content__icontains="#" + self.tag)
