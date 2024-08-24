from django.shortcuts import render, redirect

from rest_framework import generics
from main.models import *
from .serializers import *

def HomePage(request):
    return redirect("docs")

class FoodApiView(generics.ListAPIView):
    """Ma'lumotlar bazasidagi maxsulotlar ro'yxati"""
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
class FoodCreateApiView(generics.CreateAPIView):
    """Maxsulot qo'shish"""
    queryset = Food.objects.all()
    serializer_class = FoodCreateSerializer
    
class FoodDeleteApiView(generics.RetrieveDestroyAPIView):
    """Maxsulotni ID orqali olib tashlash"""
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
class FoodUpdateApiView(generics.RetrieveUpdateAPIView):
    """Maxsulotni ID orqali ma'lumotlarini yangilash"""
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
# user food

class UserFoodApiView(generics.ListAPIView):
    """Foydalanuvchi bazasidagi maxsulotlar ro'yxati"""
    queryset = UserFoodList.objects.all()
    serializer_class = UsersFoodSerializer
    
class UserFoodCreateApiView(generics.CreateAPIView):
    """Foydalanuvchi uchun maxsulot qo'shish"""
    queryset = UserFoodList.objects.all()
    serializer_class = UsersFoodSerializer
    
class UserFoodDeleteApiView(generics.RetrieveDestroyAPIView):
    """Foydalanuvchi uchun maxsulotni ID orqali olib tashlash"""
    queryset = UserFoodList.objects.all()
    serializer_class = UsersFoodSerializer
    
class UserFoodUpdateApiView(generics.RetrieveUpdateAPIView):
    """Foydalanuvchi uchun maxsulotni ID orqali ma'lumotlarini yangilash"""
    queryset = UserFoodList.objects.all()
    serializer_class = UsersFoodSerializer