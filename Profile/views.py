from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os
# Importaciones de modelos
from Profile.models import ProfileModel
from django.contrib.auth.models import User

# Importaciones de serializers
from Profile.serializers import ProfileSerializer

# Create your views here.

class ProfileTablaView(APIView):
    
    def get_object(self,pk):
        try:
            return User.objects.get(pk = pk)
        except User.DoesNotExist:
            return 0
        
    def post(self, request):
        if 'imagen' not in request.data:
            raise exceptions.ParseError("No se seleccionó el archivo a subir")
        imagen = request.data['imagen']
        userId = request.data['id_user']
        user = self.get_object(userId)
        if(user != 0):
            serializer = ProfileSerializer(data = request.data)
            if(serializer.is_valid()):
                validated_data = serializer.validated_data
                perfil = ProfileModel(**validated_data)
                perfil.save()
                serializer_response = ProfileSerializer(perfil)
                return Response(serializer_response.data, status=status.HTTP_201_CREATED)
            return Response("No permitido", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("No existe el usuario")
        
    
class ProfileTablaDetail(APIView):
    def get_object(self,pk):
        try:
            return ProfileModel.objects.get(id_user = pk)
        except ProfileModel.DoesNotExist:
            return 0
        
    def get(self,request, pk, format=None):
        idResponse = self.get_object(pk)
        if(idResponse != 0):
            idResponse = ProfileSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("sin datos", status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        image = request.data['imagen']
        idResponse = self.get_object(pk)
        if(idResponse != 0):
            serializer = ProfileSerializer(idResponse)
            try:
                os.remove('assets/'+str(idResponse.imagen))
            except os.error:
                print("Imagen no encontrada")
            idResponse.imagen = image
            idResponse.save()
            return Response("Sucess", status = status.HTTP_201_CREATED)
        else:
            return Response("Error", status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        perfil = self.get_object(pk)
        if perfil != 404:
            perfil.imagen.delete(save=True)
            return Response("Imagen eliminada",status=status.HTTP_200_OK)
        return Response("Perfil no encontrado",status = status.HTTP_400_BAD_REQUEST)
    

class UserTablaView(APIView):
    
    def get_json(self, idResponse, status):
        responseJson = {
            "first_name" : idResponse[0]['first_name'],
            "last_name" : idResponse[0]['last_name'],
            "username" : idResponse[0]['username'],
            "email" : idResponse[0]['email'],
            "status" : status
        }
        return responseJson
    
    
    def get(self,request,pk, format=None):
        user = User.objects.filter(pk = pk)
        idResponse = self.get_json(user.values(), status.HTTP_200_OK)
        return Response(idResponse)
    
    def put(self, request, pk, format=None):
        updateData = request.data
        user = User.objects.filter(pk=pk)
        user.update(username = updateData.get('username'))
        user.update(first_name = updateData.get('first_name'))
        user.update(last_name = updateData.get('last_name'))
        user.update(email = updateData.get('email'))
        return Response(self.get_json(user.values(), status.HTTP_200_OK))