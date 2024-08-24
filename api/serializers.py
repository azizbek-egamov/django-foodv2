from rest_framework import serializers
from main.models import *


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class FoodCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('nomi', 'narxi', 'rasm', 'holati',)
        
class UsersFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFoodList
        fields = "__all__"