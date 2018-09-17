from django.contrib import admin
from company.models import Review, CompanyName, CompanyAddress, CompanyContactInfo



admin.site.register(CompanyName)
admin.site.register(CompanyAddress)
admin.site.register(CompanyContactInfo)
admin.site.register(Review)
