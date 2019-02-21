from django.urls import path
from . import views

urlpatterns= [
    path('',views.index,name="index"),  #home page
    # path('newBook/',views.newBook,name="newBook"),
    # path('allBookNames/',views.allBookNames,name="allBooksNames"),
    # path('dateGreaterThan',views.dateGreaterThan,name="dateGreaterThan")

]