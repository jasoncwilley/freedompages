from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import datetime
from company.forms import ReviewForm
from company.models import CompanyName, Review
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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


def resturants(request):
    return render(request, 'resturants.html')

def products(request):
    return render(request, 'products.html')


def nightlife(request):
    return render(request, 'nightlife.html')



def religious(request):
    return render(request, 'religious.html')

def entertainment(request):
    return render(request, 'entertainment.html')


def services(request):

    return render(request, 'services.html')
