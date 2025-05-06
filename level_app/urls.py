from django.contrib import admin
from django.urls import path, include

from level_app.views import *

urlpatterns = [
    path('', get_levels, name="get_Level"),
    path('create', create_level, name="create_level"),
    path('<int:pk>/', include([
        path('', get_single_level, name="get_single_level"),
        path('detail', level_detail, name="level_detail"),
    ])),
]