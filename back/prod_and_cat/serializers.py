from rest_framework  import serializers

from .models import Product, Category, ShopProduct

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name_category', 
                )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name_product', 
                    'description', 
                    'characteristics',
                    'category',
                    )
    
    
    def create(self, validated_data):
        print(validated_data)
        return super(ProductSerializer, self).create(validated_data)


class ShopProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopProduct
        fields = ('price', 
                    'quantity', 
                    'product', 
                    'shop',
                )
