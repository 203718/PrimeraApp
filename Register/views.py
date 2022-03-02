from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


# importación de serializadores
from Register.serializer import  TablaRegisterSerializer

class PrimerRegisterView(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self, request, format=None):
        serializer =  TablaRegisterSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)