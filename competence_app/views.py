from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Competence
from .serializer import CompetenceSerializer

from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def get_competences(request):
    try:
        competences = Competence.objects.all()
        serializer = CompetenceSerializer(competences, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_competence(request):
    serializer = CompetenceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_single_competence(request, pk):
    try:
        competence = Competence.objects.get(pk=pk)
        serializer = CompetenceSerializer(competence)
        return Response(serializer.data)

    except competence.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'DELETE'])
def competence_detail(request, pk):
    try:
        competence = Competence.objects.get(pk=pk)
    except competence.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CompetenceSerializer(competence, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        competence.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)