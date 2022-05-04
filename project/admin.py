from tkinter import Menu
from django.contrib import admin

# Register your models here.

from .models import Restaurant, Customer, Cuisine, Menu_item, Reviews, MenuImages
admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Cuisine)
admin.site.register(Menu_item)
admin.site.register(Reviews)
admin.site.register(MenuImages)

