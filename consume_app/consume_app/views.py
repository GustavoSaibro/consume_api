# from django.http import JsonResponse
from . import services
from .models import Candidato
from .serializers import CandidatoSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import requests
import json


@api_view(['GET', 'POST'])
def candidato_list(request, format=None):

    if request.method == 'GET':
        services.get_candidatos()        
        candidatos = Candidato.objects.all()
        serializer =  CandidatoSerializer(candidatos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CandidatoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def candidato_detail(request, id, format=None):

    try:
        candidato = Candidato.objects.get(pk=id)
    except Candidato.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer=  CandidatoSerializer(candidato)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CandidatoSerializer(candidato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        candidato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

