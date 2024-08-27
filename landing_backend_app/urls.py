from django.urls import path
from .views import ServiceTypesListCreate, ServiceTypesDetail, MessengerTypesListCreate, MessengerTypesDetail, OrdersListCreate, OrdersDetail

urlpatterns = [
    # ServiceTypes URLs
    path('service_types/', ServiceTypesListCreate.as_view(), name='service_types-list-create'),
    path('service_types/<int:pk>/', ServiceTypesDetail.as_view(), name='service_types-detail'),

    # MessengerTypes URLs
    path('messenger_types/', MessengerTypesListCreate.as_view(), name='messenger_types-list-create'),
    path('messenger_types/<int:pk>/', MessengerTypesDetail.as_view(), name='messenger_types-detail'),

    # Orders URLs
    path('orders/', OrdersListCreate.as_view(), name='orders-list-create'),
    path('orders/<int:pk>/', OrdersDetail.as_view(), name='orders-detail'),
]
