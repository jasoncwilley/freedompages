from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

ONE_STAR = 'one star'
TWO_STARS = 'two stars'
THREE_STARS = 'three stars'
FOUR_STARS = 'four stars'
FIVE_STARS = 'five stars'
RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    )

FOOD_and_DRINKS = 'FOOD & DRINKS'
ENTERTAINMENT = 'ENTERTAINMENT'
SERVICES = 'SERVICES'
PRODUCTS = 'PRODUCTS'
RELIGIOUS_SERVICES = 'RELIGIOUS SERVICES'
OTHER = 'OTHER'
COMPANY_TYPE_CHOICES = (
    (FOOD_and_DRINKS, 'Food & Drinks'),
    (ENTERTAINMENT, 'Entertainment'),
    (SERVICES, 'Services'),
    (PRODUCTS, 'Products'),
    (RELIGIOUS_SERVICES, 'Religious Services'),
    (OTHER, 'Other'),
)
company_type = models.CharField(
    max_length=25,
    choices=COMPANY_TYPE_CHOICES,
    default=OTHER,
)

class CompanyName(models.Model):
    companyname = models.CharField(max_length=50)
    company_type = models.CharField(choices=COMPANY_TYPE_CHOICES, max_length=25)
    def __str__(self):
        return self.companyname
@receiver(post_save, sender=CompanyName)
def create_address(sender, **kwargs):
    if kwargs.get('created', False):
        CompanyAddress.objects.get_or_create(companyname=kwargs.get('instance'))
        CompanyContactInfo.objects.get_or_create(companyname=kwargs.get('instance'))



class CompanyAddress(models.Model):
    companyname = models.OneToOneField(CompanyName, related_name='address', on_delete=models.CASCADE)
    street_address = models.CharField(blank=True, null=True, max_length=50)
    city = models.CharField(max_length=25, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.IntegerField(null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)


class CompanyContactInfo(models.Model):
    companyname = models.OneToOneField(CompanyName, related_name='contact', on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True, null=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(max_length=35, blank=True, null=True)
    website = models.URLField(max_length=50, blank=True, null=True)

class Review(models.Model):
    ONE_STAR = 'one star'
    TWO_STARS = 'two stars'
    THREE_STARS = 'three stars'
    FOUR_STARS = 'four stars'
    FIVE_STARS = 'five stars'
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    FOOD_and_DRINKS = 'FOOD & DRINKS'
    ENTERTAINMENT = 'ENTERTAINMENT'
    SERVICES = 'SERVICES'
    PRODUCTS = 'PRODUCTS'
    RELIGIOUS_SERVICES = 'RELIGIOUS SERVICES'
    OTHER = 'OTHER'
    COMPANY_TYPE_CHOICES = (
        (FOOD_and_DRINKS, 'Food & Drinks'),
        (ENTERTAINMENT, 'Entertainment'),
        (SERVICES, 'Services'),
        (PRODUCTS, 'Products'),
        (RELIGIOUS_SERVICES, 'Religious Services'),
        (OTHER, 'Other'),
    )
    companyname = models.ForeignKey(CompanyName, related_name='review', on_delete=models.CASCADE)
    company_type = models.CharField(choices=COMPANY_TYPE_CHOICES, max_length=25)
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=25)
    comment = models.TextField(blank=True, max_length=500)
    rating = models.IntegerField(choices=RATING_CHOICES)
    pub_date =  models.DateTimeField(auto_now=True)
