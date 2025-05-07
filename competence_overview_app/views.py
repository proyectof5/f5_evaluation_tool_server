from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CompetenceOverview
from .serializer import CompetenceOverviewSerializer

from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def get_competences_overview(request):
    try:
        competences_overview = CompetenceOverview.objects.all()
        serializer = CompetenceOverviewSerializer(competences_overview, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_competence_overview(request):
    serializer = CompetenceOverviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_single_competence_overview(request, pk):
    try:
        competence_overview = CompetenceOverview.objects.get(pk=pk)
        serializer = CompetenceOverviewSerializer(competence_overview)
        return Response(serializer.data)

    except competence_overview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'DELETE'])
def competence_overview_detail(request, pk):
    try:
        competence_overview = CompetenceOverview.objects.get(pk=pk)
    except competence_overview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CompetenceOverviewSerializer(competence_overview, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        competence_overview.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)