from django.db import models

# Create your models here.

class Profile(models.Model):
    '''represents a facebook-like profile of a person'''
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_URL = models.URLField(blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name} \n City: {self.city} \n Email: {self.email_address}'