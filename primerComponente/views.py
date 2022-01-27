
import imp
from tkinter import NO
from rest_framework.views import APIView
from rest_framework.response import APIView

# Importaciones de modelos 
from primerComponente.models import PrimerModelo

# Importaciones de serializadores
from primerComponente.serializer import PrimerTablaSerializer

class PrimerViewList(APIView):
    def get(self, request, format=None):
        querySet = PrimerModelo.objects.all()
        serializer=PrimerTablaSerializer(query,maty=True, context={'request':request})
        return Response(serializer.data)

    def post(sefl, request, format=None):
        serializer=PrimerTablaSerializer(data=request.data, context={'request':request}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_201_CREATED)

class PrimerViewDetail(APIView):

    def get_object(self, pk):
        try:
            return PrimerModelo.object.get(pk=pk)
        except PrimerModelo.DoesNotExist:
            return 404

    def get(sel, request, pk, format=None)
        idResponse = self.get_object(pk)
        serializer = PrimerTablaSerializer(idResponse, context={'request':request})
        if idResponse ! = 404:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('No Encontrado', status=status.HTTP_BAD_REQUEST)

def put(self, request, pk, format=None):
    idResponse = self.get_object(pk)
    if idResponse != 404:
        serializer =PrimerTablaSerializer(idResponse, dta=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    else:
        return Response('Id no encontrado', status = status.HTTP_400_BAD_REQUEST)