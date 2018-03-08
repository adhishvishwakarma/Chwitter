from django.shortcuts import render
# Create your views here.

from .models import HashTag


def hashtag_view(request, hashtag):
    obj, created = HashTag.objects.get_or_create(tag=hashtag)
    return render(request, 'hashtags/tag_view.html', {"obj": obj})
