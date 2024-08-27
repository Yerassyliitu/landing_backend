from django.contrib import admin
from .models import MessengerTypes, ServiceTypes, Orders

admin.site.register(Orders)
admin.site.register(MessengerTypes)
admin.site.register(ServiceTypes)

