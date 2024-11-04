from django.shortcuts import render
from api import serializer as api_serializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from userauths.models import User

# Create your views here.

#get token using serializer_class defined in api_serializer.MyTokenObtainPairSerializer
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = api_serializer.MyTokenObtainPairSerializer

#generics: generics refers to a module that provides generic views — reusable, pre-configured views for common actions like creating, retrieving, updating, and deleting resources.
#use createApiview to handle post request to create new instance
class RegisterView(generics.CreateAPIView):
    #required to call User model due to generic views although not directly used
    queryset = User.objects.all()
    #allow everyone to register
    permission_class = [AllowAny]
    serializer_class = api_serializer.RegisterSerializer