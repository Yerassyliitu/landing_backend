from django.db import models

class ServiceTypes(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class MessengerTypes(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Orders(models.Model):
    service_type = models.ForeignKey(ServiceTypes, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255, null=False)
    project_name = models.CharField(max_length=255, null=False)
    messenger_type = models.ForeignKey(MessengerTypes, on_delete=models.CASCADE, default=1)
    contact = models.CharField(max_length=255, null=False)
    budget = models.IntegerField(null=False)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name + ' - ' + self.project_name