from django.urls import path
from . import views
from company.views import nightlife, companyinfo

app_name='company'
urlpatterns = [

    path('', views.index, name='index'),
    path('foodandbev/', views.foodandbev, name='foodandbev'),
    path('nightlife/', views.nightlife, name='nightlife'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('services/', views.services, name='services'),
    path('religious/', views.religious, name='religious'),
    path('products/', views.products, name='products'),
    path('companyinfo/', views.companyinfo, name='companyinfo'),
    path('contactinfo/', views.contactinfo, name='contactinfo'),
    path('directions/', views.directions, name='directions'),
    path('reviews/', views.reviews, name='reviews'),
    path('promotions/', views.promotions, name='promotions'),
    path('map/', views.map, name='map'),
    path('d/', views.ReviewCreate.as_view(), name='review')
]
