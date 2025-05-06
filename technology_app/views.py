from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Technology
from .serializer import TechnologySerializer

from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def get_technologies(request):
    try:
        technology = Technology.objects.all()
        serializer = TechnologySerializer(technology, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_technology(request):
    serializer = TechnologySerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_single_technology(request, pk):
    try:
        technology = Technology.objects.get(pk=pk)
        serializer = TechnologySerializer(technology)
        return Response(serializer.data)

    except technology.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'DELETE'])
def technology_detail(request, pk):
    try:
        technology = Technology.objects.get(pk=pk)
    except technology.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TechnologySerializer(technology, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        technology.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)