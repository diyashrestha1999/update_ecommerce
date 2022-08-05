from .models import *

from rest_framework import serializers

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vendor
        fields= ['id','name', 'number', 'username', 'password', 'email']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields= '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model= Shop
        fields= '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields= '__all__'