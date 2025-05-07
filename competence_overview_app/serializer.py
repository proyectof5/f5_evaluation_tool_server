from rest_framework import serializers
from .models import CompetenceOverview

class CompetenceOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetenceOverview
        fields = '__all__'