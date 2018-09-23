from django.urls import path
from . import views
from company.views import nightlife, DetailView, companyinfo, CompanyContactInfo, CompanyHours, ReviewList, CompanyReviews
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
#    path('reviews/', views.reviews, name='reviews'),
    path('promotions/', views.promotions, name='promotions'),
    path('map/', views.map, name='map'),
    path('d/', views.ReviewCreate.as_view(), name='review'),
    path('<int:pk>/', DetailView.as_view(), name= 'detail'),
    path('companycontactinfo_detail/(int:pk>', CompanyContactInfo.as_view(), name='companycontactinfo_detail'),
    path('companyhours_detail/<int:pk>', CompanyHours.as_view(), name= 'companyhours_detail'),
    path('reviews', ReviewList.as_view()),
    path('reviews/<int:id>/', CompanyReviews.as_view()),
    path('companyreviews/', CompanyReviews.as_view()),
    path('company/<int:companyname_id>', views.companyname_detail, name='companyname_detail'),
    path('companyname/<int:companyname_id>/add_review/', views.add_review, name='add_review'),
    path('review/(<int:review_id>', views.review_detail, name='review_detail'),
    path('companyname', views.companyname_list, name='companyname_list'),

]
