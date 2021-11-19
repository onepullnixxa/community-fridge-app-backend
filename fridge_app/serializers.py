from rest_framework import serializers
from .models import Fridge

class FridgeSerializer(serializers.HyperlinkedModelSerializer):
    fridge_url = serializers.ModelSerializer.serializer_url_field(
        view_name='fridge_detail'
    )

    class Meta:
        model = Fridge
        fields = ('id', 'fridge_url', 'fridge_name', 'image_url', 'needs_cleaning', 'canned_foods_needed', 'produce_needed', 'fruits_needed', 'maintenance_needed',)