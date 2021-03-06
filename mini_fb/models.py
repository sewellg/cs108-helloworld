from django.db import models
from django.urls import reverse


# Create your models here.

class Profile(models.Model):
    '''represents a facebook-like profile of a person'''
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_URL = models.URLField(blank=True)
    birthday = models.DateField(blank=True)
    friends = models.ManyToManyField("self")


    def get_absolute_url(self):
        return reverse('profiles', kwargs={'pk':Profile.pk})

    def __str__(self):
        return f'{self.last_name}, {self.first_name} \n City: {self.city} \n Email: {self.email_address}'

    def get_status_messages(self):
        return StatusMessage.objects.filter(profile=self)

    def get_friends(self):

        friends = self.friends.all()
        print(friends)
        return friends

    def get_news_feed(self):
        news = StatusMessage.objects.all().order_by("-timestamp")
        friends = self.friends.all()
        friend_news = StatusMessage.objects.filter(profile__in=friends)
        return friend_news

    def get_friend_suggestions(self):
        possible_friends = Profile.objects.exclude(pk__in=self.friends.all()).exclude(pk=self.pk)
        return possible_friends


class StatusMessage(models.Model):
    timestamp = models.DateTimeField(blank=False)
    message = models.TextField(blank=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.timestamp}\n {self.message}\n {self.profile}'


    