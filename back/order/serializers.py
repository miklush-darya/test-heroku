from rest_framework  import serializers

from .models import Order, ShopProductOrder

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 
            )

class ShopProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopProductOrder
        fields = ('order',
                    'shopproduct',
            )
