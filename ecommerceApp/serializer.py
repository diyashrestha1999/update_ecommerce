
from dataclasses import fields
from operator import truediv
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

    def get_fields(self):
        fields= super().get_fields()
        if self.context['request'].method=='GET':
            # import ipdb; ipdb.set_trace();
            fields['owner'] = VendorSerializer()

        return fields

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= '__all__'

    def get_fields(self):
        fields= super().get_fields()
        if self.context['request'].method=='GET':
            fields['category'] = CategorySerializer()
            fields['shop'] = ShopSerializer(many=True)
        return fields

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields= '__all__'
    
    def get_fields(self):
        fields= super().get_fields()
        if self.context['request'].method=='GET':
            fields['customer'] = CustomerSerializer()

        return fields

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderDetail
        fields= '__all__'


    def get_fields(self):
        fields= super().get_fields()
        if self.context['request'].method=='GET':
            fields['product'] = ProductSerializer()
            fields['order'] = OrderSerializer()

        return fields



class ProductInCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= '__all__'

    def get_fields(self):
        fields= super().get_fields()
        if self.context['request'].method=='GET':
            fields['category'] = CategorySerializer()
            

        return fields

class ProductInShopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'   

    def get_fields(self):
        fields=super().get_fields()
        if self.context['request'].method=='GET':
            fields['shop']=ShopSerializer(many=True)

        return fields

        
    