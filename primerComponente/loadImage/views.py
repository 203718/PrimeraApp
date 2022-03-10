from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
import datetime

# importación de modelos
from loadImage.models import ImageModel

# importación de serializadores
from loadImage.serializers import serializerLoadImage, serializerLoadImage2

class PrimerViewList(APIView):
    def get(self, request, format=None):
        querySet = ImageModel.objects.all()
        serializer=serializerLoadImage(querySet,many=True, context={'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer=serializerLoadImage2(data=request.data, context={'request':request})
        archivo = request.data['name_img']
        
        if serializer.is_valid():
            serializer.create(archivo)
            return Response({'Messages':'Success'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Messages':'Error'}, status=status.HTTP_400_BAD_REQUEST)

class PrimerViewDetail(APIView):

    def get_object(self, pk):
        try:
            return ImageModel.objects.get(pk=pk)
        except ImageModel.DoesNotExist:
            return 404

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            serializer = serializerLoadImage(idResponse, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('Not Found', status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404: 
            serializer = serializerLoadImage2(idResponse, data = request.data, context={'request':request}) 
            if serializer.is_valid():
                try: 
                    os.remove('assets/'+str(idResponse.name_img))
                except os.error:
                    print ('error')
                idResponse.name_img=(request.data['name_img'])
                idResponse.url_img='http://localhost:8000/assets/'+str(request.data['name_img'])
                idResponse.format_img=str(request.data['name_img']).split(".")[1]
                idResponse.edited=datetime.datetime.now()
                idResponse.save()
                return Response("Succes", status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('id not found', status=status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse !=404:
            serializer = serializerLoadImage2(idResponse, data= request.data , context={'request': request})
            if serializer.is_valid():
                try: 
                    os.remove('assets/'+str(idResponse.name_img))
                except os.error:
                    print ('error')
                idResponse.delete()
                return Response('Success',status = status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Id not found',status = status.HTTP_400_BAD_REQUEST)    
