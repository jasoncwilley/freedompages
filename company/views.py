from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse



def index(request):
    return render(request, 'index.html')

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
