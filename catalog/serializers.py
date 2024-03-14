from rest_framework import serializers
from catalog.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'description', 'is_active', 'meta_keywords',
                  'meta_description', 'created_at', 'updated_at')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'slug', 'brand', 'sku', 'price', 'old_price', 'image', 'is_active',
                  'is_bestseller', 'is_featured', 'quantity', 'description', 'meta_keywords',
                  'meta_description', 'created_at', 'updated_at', 'categories')
