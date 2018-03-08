from django.urls import path
from .views import hashtag_view


urlpatterns = [
    path('<hashtag>/', hashtag_view, name='hashtag'),
]
