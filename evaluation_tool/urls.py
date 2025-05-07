"""
URL configuration for evaluation_tool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({"message": "API evaluation 0.0.10"})

urlpatterns = [
    path('', api_root),
    path('v1/', include([
        path('competences/', include('competence_app.urls')),
        path('technologies/', include('technology_app.urls')),
        path('categories/', include('category_app.urls')),
        path('levels/', include('level_app.urls')),
        path('overviews/', include('competence_overview_app.urls')),
    ])),
]

