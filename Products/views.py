from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Products.models import Product
from Products.models import User
from django.contrib.auth import authenticate, login, logout
import re
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.
for user in User.objects.all():
    Token.objects.get_or_create(user=user)
            
            
class SignUp(APIView):
    def post(self, request):
        try:
            username = request.query_params.get('username')
            password = request.query_params.get('password')
            email = request.query_params.get('email')
            if not self.validate_email(email= email):
                return Response(data='invalid email', status=400)
            mobile_number = request.query_params.get('mobile_number')
            if not self.validate_mobile_num(mobile_number=str(mobile_number)):
                return Response(data='invalid Mobile Number', status=400)
            first_name = request.query_params.get('first_name')
            last_name = request.query_params.get('last_name')
            user_object = User(username = username, password= password, email=email, mobile_number= mobile_number, first_name= first_name, last_name= last_name)
            user_object.save()
            return Response (data= 'Registered successfully', status =200)
        except:
            return Response(data='invalid entry', status=400)
        
    def validate_email(self, email):  
        if re.match(r"[^@]+@[^@]+\.[^@]+", email): 
            return True  
        return False  
    
    def validate_mobile_num(self, mobile_number):
        if re.fullmatch(r'^\d{10}$', mobile_number):
           return True
        return False
    
     
class LoginView(APIView):
    def post(self, request):
        try:
            username= request.query_params.get('username')
            password = request.query_params.get('password')
            User.objects.get(username=username, password=password)
            return Response(data='login successful', status= 200)
        except:
            return Response(data='invalid credentials', status =400)
    
    
       
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(data='Successfully Logged out', status=200)


class GetProductList(APIView):
    def get(self,request):
        print('request data',request.query_params.get('id'))
        product_list=Product.objects.all().values()
        return Response(data=product_list, status=status.HTTP_200_OK)
        
        

       
class SearchProduct(APIView):
    def get(self, request):
        try:
            name= request.query_params.get('name')
            t_object= Product.objects.filter(name__contains=name).values()
            return Response(data= t_object,status=200)
        except:
            return Response(data='invalid entry', status=400)



