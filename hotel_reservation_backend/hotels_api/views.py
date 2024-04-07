from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hotel
from .serializers import HotelSerializers
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import filters


#testing the view
def home(request):
    return HttpResponse("<h1> TESTING HOME SCREEN </h1>")

#Defining get and post for the hotellist
class HotelListCreate(APIView):
    def get(self, request, format=None):
        hotels = Hotel.objects.all()
        serializer = HotelSerializers(hotels, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HotelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)