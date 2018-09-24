from .models import CompanyName
import django_filters

class CompanyNameFilter(django_filters.FilterSet):
    class Meta:
        model = CompanyName
        fields = {
        'companyname': ['icontains',],
        'company_type': ['exact', ],
        }
