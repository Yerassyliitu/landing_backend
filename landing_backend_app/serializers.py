from rest_framework import serializers
from .models import ServiceTypes, MessengerTypes, Orders

class ServiceTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTypes
        fields = '__all__'

class MessengerTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessengerTypes
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    service_types = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=ServiceTypes.objects.all()
    )

    class Meta:
        model = Orders
        fields = '__all__'
