from rest_framework import serializers
from loadImage.models import ImageModel

class serializerLoadImage(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ('__all__')

class serializerLoadImage2(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ('name_img',)

    def create (self, archivo):
        nombreArchivo = str (archivo)
        formato = nombreArchivo.split(".")[1]
        url = 'http://localhost:8000/assets/img/' + nombreArchivo
        query = ImageModel.objects.create(name_img = archivo, format_img = formato, url_img = url)
    
     