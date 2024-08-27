# Create your views here.
from rest_framework import generics
from .models import ServiceTypes, MessengerTypes, Orders
from .serializers import ServiceTypesSerializer, MessengerTypesSerializer, OrdersSerializer

# ServiceTypes CRUD
class ServiceTypesListCreate(generics.ListCreateAPIView):
    queryset = ServiceTypes.objects.all()
    serializer_class = ServiceTypesSerializer

class ServiceTypesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceTypes.objects.all()
    serializer_class = ServiceTypesSerializer

# MessengerTypes CRUD
class MessengerTypesListCreate(generics.ListCreateAPIView):
    queryset = MessengerTypes.objects.all()
    serializer_class = MessengerTypesSerializer

class MessengerTypesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MessengerTypes.objects.all()
    serializer_class = MessengerTypesSerializer

# Orders CRUD
class OrdersListCreate(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
