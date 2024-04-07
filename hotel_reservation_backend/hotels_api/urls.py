from django.urls import path
from . import views
from .views import HotelListCreate

urlpatterns= [
    path("home/", views.home, name="home"),
    path('hotels/', HotelListCreate.as_view(), name='hotel-list-create'),
]