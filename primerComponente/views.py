from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# importación de modelos
from primerComponente.models import PrimerModelo

# importación de serializadores
from primerComponente.serializer import PrimerTablaSerializer

class CustomedResponse():

    def response_custom(self, validate_data, responseCustomed, status):
        response = {
            "messages":responseCustomed,
            "payload":{"data":validate_data},
            "status":status
        }
        return response

class PrimerViewList(APIView):
    def get(self, request, format=None):
        querySet = PrimerModelo.objects.all()
        serializer=PrimerTablaSerializer(querySet,many=True, context={'request':request})
        response_custom = CustomedResponse()
        return Response(response_custom.response_custom(serializer.data, 'success', status = status.HTTP_200_OK))

    def post(self, request, format=None):
        serializer=PrimerTablaSerializer(data=request.data, context={'request':request})
        response_custom = CustomedResponse()
        if serializer.is_valid():
            serializer.save()
            return Response(response_custom.response_custom(serializer.data, 'Success', status.HTTP_201_CREATED))
        else:
            return Response(response_custom.response_custom(serializer.errors, 'Error', status.HTTP_400_BAD_REQUEST))

class PrimerViewDetail(APIView):

    def get_object(self, pk):
        try:
            return PrimerModelo.objects.get(pk=pk)
        except PrimerModelo.DoesNotExist:
            return 404

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        response_custom = CustomedResponse()
        #serializer = PrimerTablaSerializer(idResponse, context={'request':request})
        if idResponse != 404:
            serializer = PrimerTablaSerializer(idResponse, context={'request':request})
            return Response(response_custom.response_custom(serializer.data, 'Success', status.HTTP_200_OK))
        else:
            return Response(response_custom.response_custom('Not Found','Error', status=status.HTTP_400_BAD_REQUEST))

    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        response_custom = CustomedResponse()
        if idResponse != 404:
            serializer =PrimerTablaSerializer(idResponse, data=request.data, context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(response_custom.response_custom(serializer.data,'Success',status = status.HTTP_200_OK))
            else:
                return Response(response_custom.response_custom(serializer.errors,'Error',status = status.HTTP_400_BAD_REQUEST))
        else:
            return Response(response_custom.response_custom('Id no encontrado','Error',status = status.HTTP_400_BAD_REQUEST))


    def delete (self, request, pk, format=None):
        idResponse = self.get_object(pk)
        response_custom = CustomedResponse()
        if idResponse !=404:
            serializer = PrimerTablaSerializer(idResponse, data= request.data , context={'request': request})
            if serializer.is_valid():
                idResponse.delete()
                return Response(response_custom.response_custom(serializer.data,'Success',status = status.HTTP_200_OK))
            else:
                return Response(response_custom.response_custom(serializer.errors,'Error',status = status.HTTP_400_BAD_REQUEST))
        else:
            return Response(response_custom.response_custom('Id no encontrado','Error',status = status.HTTP_400_BAD_REQUEST))    