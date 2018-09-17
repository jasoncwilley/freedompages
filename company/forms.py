from django import forms
from company.models import CompanyName

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
class ReviewForm(forms.ModelForm):

    #id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    companyname = forms.ModelChoiceField(queryset=CompanyName.objects.all(), empty_label="(Company Name)")
    first_name = forms.CharField( max_length=50)
    last_name = forms.CharField( max_length=25)
    comment = forms.CharField( max_length=500)
    rating = forms.ChoiceField(choices=RATING_CHOICES)

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
    companyname = forms.ModelChoiceField(queryset=CompanyName.objects.all(), to_field_name='companyname',empty_label="(Company Name)")
    class Meta:
        model = CompanyName
        fields = ('companyname', 'first_name', 'last_name', 'comment', 'rating')

    def save(self):
        x = ReviewForm(request.POST)
        x.save()
