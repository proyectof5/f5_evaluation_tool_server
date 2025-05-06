from django.contrib import admin
from django.urls import path, include

from category_app.views import *

urlpatterns = [
    path('', get_categories, name="get_categories"),
    path('create', create_category, name="create_category"),
    path('<int:pk>/', include([
        path('', get_single_category, name="get_single_category"),
        path('detail', category_detail, name="category_detail"),
    ])),
]