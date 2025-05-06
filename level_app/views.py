from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Level
from .serializer import LevelSerializer

from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def get_levels(request):
    try:
        level = Level.objects.all()
        serializer = LevelSerializer(level, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_level(request):
    serializer = LevelSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_single_level(request, pk):
    try:
        level = Level.objects.get(pk=pk)
        serializer = LevelSerializer(level)
        return Response(serializer.data)

    except level.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'DELETE'])
def level_detail(request, pk):
    try:
        level = Level.objects.get(pk=pk)
    except level.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = LevelSerializer(level, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        level.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)