from django.contrib import admin
from django.urls import path, include

from technology_app.views import *

urlpatterns = [
    path('', get_technologies, name="get_technologys"),
    path('create', create_technology, name="create_technology"),
    path('<int:pk>/', include([
        path('', get_single_technology, name="get_single_technology"),
        path('detail', technology_detail, name="technology_detail"),
    ])),
]