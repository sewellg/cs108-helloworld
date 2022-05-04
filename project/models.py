from django.db import models

class Menu_item(models.Model):
    '''a given food on a restaurant's menu'''
    name = models.CharField(blank=False, max_length=200)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    '''restaurants in the bu area'''
    rescuisine = models.ForeignKey('Cuisine', on_delete=models.CASCADE) #cuisine
    name = models.CharField(blank=False, max_length=200) #name
    price_range = models.CharField(blank=False, max_length=5) #price based off yelp
    mon_times = models.TextField(blank=False)
    tue_times = models.TextField(blank=False)
    wed_times = models.TextField(blank=False)
    thur_times = models.TextField(blank=False)
    fri_times = models.TextField(blank=False)
    sat_times = models.TextField(blank=False)
    sun_times = models.TextField(blank=False)
    email_contact = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    number = models.CharField(blank=True, max_length=20)
    item = models.ManyToManyField(Menu_item) #all menu items
    address = models.CharField(blank=False, max_length=250) #location
    image = models.URLField(blank=True) #image for restaurant

    def find_recommendations(self):
        '''recommends restaurants of the same cuisine'''
        cuisinename = self.rescuisine
        res = Restaurant.objects.filter(rescuisine = cuisinename).exclude(pk=self.pk)
        
        return res

    def get_reviews(self):
        '''returns all restaurant reviews'''
        return Reviews.objects.filter(restaurant=self)

    def get_menu(self):
        '''returns restaurant's menu items'''
        menu = self.item.all()
        return menu
        
    def get_menu_pics(self):
        '''returns restaurant menu images'''
        return MenuImages.objects.filter(restaurant=self)

    def __str__(self) -> str:
        return self.name

class Cuisine(models.Model):
    '''defines a cuisine for each restaurant'''
    name = models.CharField(blank=False, max_length=100)
    def __str__(self) -> str:
        return self.name

class Customer(models.Model):
    ''''''
    name = models.TextField(blank=False)
    favorites = models.ManyToManyField(Restaurant)
    cuisines = models.ManyToManyField(Cuisine)
    def __str__(self) -> str:
        return self.name

class Reviews(models.Model):
    '''creates reviews for restaurants'''

    STARS = [
    ('1/5', "1 Star"),
    ('2/5', "2 Stars"),
    ('3/5', "3 Stars"),
    ('4/5', "4 Stars"),
    ('5/5', "5 Stars")
    ]
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=200)
    stars = models.CharField(blank=False, max_length=20, choices=STARS, default='1/5')
    content = models.TextField(blank=False)
    def __str__(self) -> str:
        return self.name

class MenuImages(models.Model):
    '''images for restaurant menus'''
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    img = models.URLField(blank=False)
    def __str__(self) -> str:
        return self.img


# Create your models here.
