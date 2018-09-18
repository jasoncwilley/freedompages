from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import datetime
from company.forms import ReviewForm
from company.models import CompanyName, Review, CompanyContactInfo, CompanyHours
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views import generic



class CompanyHours(generic.DetailView):
    model = CompanyHours
def companyhours_detail(request, pk):
    try:
        company = CompanyHours.objects.get(pk=pk)
    except CompanyHours.DoesNotExist:
        raise Http404('Company Does Not Exist In Our Database')
    return render(request, 'companyhours_detail.html', context= {'company': company})



class CompanyContactInfo(generic.DetailView):
    model = CompanyContactInfo
    context = 'contactinfo'
def companycontactinfo_detail(request, pk):
    try:
        company = CompanyContactInfo.objects.get(pk=pk)
    except CompanyContactInfo.DoesNotExist:
        raise Http404('Company Does Not Exist In Our Database')
    return render(request, 'companycontactinfo_detail.html', context= {'company': company})

class ReviewCreate(CreateView):
    model = Review
    fields = '__all__'
    def get_success_url(self):
        return HttpResponseRedirect('/index/')
'''
def submit_review(request):
    review_form = ReviewForm
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            Review.save()
            return HttpResponseRedirect(reverse('not a registered company'))
    else:
        review_form = ReviewForm()
    context = {
    'review_form': review_form,
    }

    return render(request, 'review.html', context)
'''


def index(request):
    return render(request, 'index.html')

def map(request):
    return render(request, 'map.html')

def userloc(request):
    ip = get_client_ip(request)
    ip = '74.136.205.106'
    print(ip)
    reader = geoip2.database.Reader('/home/minty/Documents/Chatango-front-end/GeoLite2-City.mmdb')
    response = reader.city(str(ip))
    city = response.city.name
    latitude = response.location.latitude
    longitude = response.location.longitude
    return HttpResponse("Your IP address is " + str(ip) + "\n" + "Your city is " + str(city) + "/n" + "Your longitude is " + str(longitude) +  "/n" + "Your latitude is" + str(latitude))

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def contactinfo(request):
    return render(request, 'contactinfo.html')

def directions(request):
    return render(request, 'directions.html')

def reviews(request):
    return render(request, 'reviews.html')

def promotions(request):
    return render(request, 'promotions.html')

def companyinfo(request):
    return render(request, 'companyinfo.html')


def foodandbev(request):
    companies = CompanyName.objects.all()
    company = companies.filter(company_type='FOOD & DRINKS')
    context = {
        'company': company,
    }
    return render(request, 'foodandbev.html', context)

def products(request):
    companies = CompanyName.objects.all()
    company = companies.filter(company_type='PRODUCTS')
    context = {
        'company': company,
    }
    return render(request, 'products.html', context)

def nightlife(request):
    companies = CompanyName.objects.all()
    company = companies.filter(company_type='NIGHTLIFE')
    context = {
        'company': company,
    }
    return render(request, 'nightlife.html', context)

def religious(request):
    companies = CompanyName.objects.all()
    company = companies.filter(company_type='RELIGIOUS SERVICES')
    context = {
        'company': company,
    }
    return render(request, 'religious.html', context)

def entertainment(request):
    companies = CompanyName.objects.all()
    company = companies.filter(company_type='ENTERTAINMENT')
    context = {
        'company': company,
    }
    return render(request, 'entertainment.html', context)

def services(request):
    companies = CompanyName.objects.all()
    company = companies.filter(company_type='SERVICES')
    context = {
        'company': company,
    }
    return render(request, 'services.html', context)
