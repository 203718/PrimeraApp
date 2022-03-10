from rest_framework import serializers

from Profile.models import ProfileModel

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProfileModel
        fields = ('__all__')