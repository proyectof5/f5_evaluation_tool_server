from django.contrib import admin
from django.urls import path, include

from competence_app.views import *

urlpatterns = [
    path('', get_competences, name="get_competences"),
    path('create', create_competence, name="create_competence"),
    path('<int:pk>/', include([
        path('', get_single_competence, name="get_single_competence"),
        path('detail', competence_detail, name="competence_detail"),
    ])),
]
