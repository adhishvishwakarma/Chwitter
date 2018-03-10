from django.urls import path
from .views import (
    view_chweets,
    list_chweets,
    create_chweet,
    update_chweet,
    delete_chweet,
    re_chweet,
)


urlpatterns = [
    path('', list_chweets, name='list'),
    path('<int:chweet_id>/', view_chweets, name='view'),
    path('new/', create_chweet, name='create'),
    path('<int:chweet_id>/update/', update_chweet, name='update'),
    path('<int:chweet_id>/delete/', delete_chweet, name='delete'),
    path('<int:chweet_id>/re/', re_chweet, name='rechweet'),
]
