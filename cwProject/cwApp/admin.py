from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Car
 #registers Book and Car for website
admin.site.register(Book)
admin.site.register(Car)
