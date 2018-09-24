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
from django.views.generic import ListView
from .forms import ReviewForm
import datetime
from django.db.models import Avg
import django_filter
from .filters import CompanyNameFilter


def search(request):
    company_list = CompanyName.objects.all()
    company_filter = CompanyNameFilter(request.GET, queryset=company_list)
    return render(request, 'company_list.html', {'filter': company_filter})



def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})
'''
def search(request):
    companies= CompanyName.objects.all()
    context = {'companies':companies}
    return render(request, 'search.html', context)
'''
def companyname_detail(request, companyname_id):
    companyname = get_object_or_404(CompanyName, pk=companyname_id)
    form = ReviewForm()
    return render(request, 'companyname_detail.html', {'companyname': companyname, 'form': form})

def add_review(request, companyname_id):
    companyname = get_object_or_404(CompanyName, pk=companyname_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = request.user.username
        review = Review()
        review.companyname = companyname
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        return HttpResponseRedirect(reverse('company:companyname_detail', args=(companyname.id,))),
    return render(request, 'companyname_detail.html', {'companyname': companyname, 'form': form})



class CompanyHours(generic.DetailView):
    model = CompanyHours
def companyhours_detail(request, pk):
    try:
        company = CompanyHours.objects.get(pk=pk)
    except CompanyHours.DoesNotExist:
        raise Http404('Company Does Not Exist In Our Database')
    return render(request, 'companyhours_detail.html', context= {'company': company})
class DetailView(generic.DetailView):
    model = CompanyContactInfo
    template_name= 'detail.html'

class CompanyContactInfo(generic.DetailView):
    model = CompanyContactInfo

def companycontactinfo_detail(request, pk):
    try:
        company = CompanyContactInfo.objects.get(pk=pk)
    except CompanyContactInfo.DoesNotExist:
        raise Http404('Company Does Not Exist In Our Database')
    return render(request, 'companycontactinfo_detail.html', context= {'company': company})



def reviews(request, companyname_id):
    average = Review.objects.all().filter(companyname_id=companyname_id).values('rating').aggregate(Avg('rating'))
    reviews = Review.objects.all().filter(companyname_id=companyname_id)

    try:
        for review in reviews:
            for name,avg in average.items():
                if int(avg) > 0:
                    avgrating=('%s' %(avg))
                    print(avgrating)


    except Review.DoesNotExist:
        raise Http404('Review Does Not Exist In Our Database')
    return render(request, 'reviews.html', context={ 'reviews': reviews, 'avg':avg})




def add_review(request):
    form = ReviewForm(request.method=="POST") or ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/')
    else:
        form = ReviewForm()
        context = {
        'form': form,
        }
        return render(request, 'addreview.html', context)



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


def directions(request):
    return render(request, 'directions.html')



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
