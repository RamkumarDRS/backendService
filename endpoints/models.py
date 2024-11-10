from django.db import models
class ServiceProvider(models.Model):

    serviceType = models.IntegerField(primary_key=True,unique=True)
    ServiceProvider = models.CharField(max_length=100)
    key= models.CharField(max_length=100)
    api1 = models.CharField(max_length=100)
    api2 = models.CharField(max_length=100)
    status = models.BooleanField()

    class Meta:
        db_table = 'service_table'

    def __int__(self):
        return self.serviceType
