# file: forms.py
# author: Grace Sewell
# description: forms for final project
from django import forms   
from .models import Reviews, Restaurant

# star rating for restaurants:
STARS = [
    ('1/5', "1 Star"),
    ('2/5', "2 Stars"),
    ('3/5', "3 Stars"),
    ('4/5', "4 Stars"),
    ('5/5', "5 Stars")
]

class CreateReviewForm(forms.ModelForm):
    '''creates a new review for a given restaurant'''
    name = forms.CharField(label="Name", required=True) #reviewer
    content = forms.CharField(label="Review", required=True) #review
    stars = forms.CharField(label="How many stars?", widget=forms.Select(choices=STARS)) #ranking
    
    class Meta:
        model = Reviews
        fields = ["name", "content", "stars"]