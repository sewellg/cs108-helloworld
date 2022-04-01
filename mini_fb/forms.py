from socket import fromshare
from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=range(2012, 1900, -1),),)
    city = forms.CharField(label="Hometown", required=False)
    email = forms.CharField(label="Email", required=False)
    image_url = forms.CharField(label="Image URL", required=False)

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "birthday", "city", "email", "image_url"]

class UpdateProfileForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=range(2012, 1900, -1),),required=False)
    city = forms.CharField(label="Hometown", required=False)
    email = forms.CharField(label="Email", required=False)
    image_url = forms.CharField(label="Image URL", required=False)

    class Meta:
        model = Profile
        fields = ["birthday", "city", "email", "image_url"]
