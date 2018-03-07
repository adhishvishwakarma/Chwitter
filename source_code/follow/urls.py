from django.urls import path
from .views import user_detail, user_follow


urlpatterns = [
    path('<username>/', user_detail, name="user_detail"),
    path('<username>/following/', user_follow, name="user_follow"),
]
