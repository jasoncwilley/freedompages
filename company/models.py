from django.db import models
from django_google_maps import fields as map_fields



class CompanyName(models.Model):
    companyname = models.CharField(max_length=50)
    def __str__(self):
        return self.companyname

class CompanyAddress(models.Model):
    companyname = models.ForeignKey(CompanyName, on_delete=models.CASCADE)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
