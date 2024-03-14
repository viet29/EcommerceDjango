from rest_framework import serializers
from cart.models import *


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('date_added', 'quantity', 'product')
