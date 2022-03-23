from django.db import models

# Create your models here.

class Quote(models.Model):
    '''represents a quote from a famous person'''

    text = models.TextField(blank=True)
    author = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''return a formatted string of this quote'''
        return f'"{self.text}" - {self.author}'
        