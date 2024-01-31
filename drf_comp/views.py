from django.shortcuts import render, get_object_or_404
from comp_app.models import Computer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CompSerializer


# Create your views here.

class CompViewSet(viewsets.ModelViewSet):
    serializer_class = CompSerializer
    queryset = Computer.objects.all()

@api_view(['GET', 'PUT', 'DELETE'])
def get_computer(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    if request.method == 'GET':
        serializer = CompSerializer(computer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = request.data
        serializer = CompSerializer(computer, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        computer.delete()
        return Response(status=204)


