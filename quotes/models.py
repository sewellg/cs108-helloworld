##### quotes/models.py #####

from django.db import models
import random
from django.urls import reverse

class Person(models.Model):
    '''Encapsulate the concept of a person, who said some famous quote.'''

    name = models.TextField(blank=False)
    
    def __str__(self):
        '''Return a string representaton of this Person.'''
        return self.name

    def get_random_image(self):
        '''Return an image of this person, selected at random.'''

        # find all images for this person:
        images = Image.objects.filter(person=self)

        # select one at random to return
        return random.choice(images)

    def get_all_quotes(self):
        '''Return all quotes for this Person.'''

        # use the object manager to filter Quotes by this person's pk:
        return Quote.objects.filter(person=self)

    def get_all_images(self):
        '''Return all images for this Person.'''

        # use the object manager to filter Image by this person's pk:
        return Image.objects.filter(person=self)
      
class Quote(models.Model):
    '''Encapsulate the idea of a quote (i.e., text).'''

    # data attributes of a quote:
    text = models.TextField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def get_absolute_url(self):
        '''Return a URL to display this quote object.'''
        return reverse("quote", kwargs={"pk": self.pk})
    
    

    def __str__(self):
        '''Return a string representation of this Quote object.'''
        return f'"{self.text}" - {self.person}'

class Image(models.Model):
    '''Represent an image URL for a Person.'''

    image_url = models.URLField(blank=True)
    image_file = models.ImageField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        '''Return the image url of this Image.'''

        # if we have stored an actual image object:
        if self.image_file:
            return self.image_file.url
        # otherwise, return the URL to an image stored elsewhere
        else:
            return self.image_url