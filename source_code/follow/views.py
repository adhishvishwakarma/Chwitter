from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()


def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    context = {'object': user}
    return render(request, "follow/user_detail.html", context)


def user_follow(request, username):
    toggle_user = get_object_or_404(User, username__iexact=username)
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        if toggle_user in user_profile.following.all():
            user_profile.following.remove(toggle_user)
        else:
            user_profile.following.add(toggle_user)
    return redirect("user_detail", username=username)
