from django.contrib import admin
from django.urls import path, include

from competence_overview_app.views import *

urlpatterns = [
    path('', get_competences_overview, name="get_competences_overview"),
    path('create', create_competence_overview, name="create_competence"),
    path('<int:pk>/', include([
        path('', get_single_competence_overview, name="get_single_competence_overview"),
        path('detail', competence_overview_detail, name="competence_overview_detail"),
    ])),
]