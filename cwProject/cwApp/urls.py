from django.urls import path
from . import views

urlpatterns= [
    #Books paths
    path('',views.index,name="index"),  #home page
    path('newBook1/',views.newBook1,name="newBook1"),
    path('newBook2/',views.newBook2,name="newBook2"),
    path('allBookNames/',views.allBookNames,name="allBooksNames"),
    path('dateLessThan/',views.dateLessThan,name="dateGreaterThan"),
   #Car views
    path('newCar1/',views.newCar1,name="newCar1"),
    path('newCar2/',views.newCar2,name='newCar2'),
    path('allYears/',views.allYears,name='allYears'),
    path('post2010/',views.post2010,name='post2010')
]