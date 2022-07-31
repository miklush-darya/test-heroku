from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import generics, viewsets, mixins
from .models import Category, Product, ShopProduct
from .serializers import CategorySerializer, ProductSerializer, ShopProductSerializer


class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def post(self, request):
    #     serializer = CategorySerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'new_category': serializer.data})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category']


##############
# class ProductAPIView(mixins.CreateModelMixin):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#################

class ShopProductApiView(viewsets.ModelViewSet):
    queryset = ShopProduct.objects.all()
    serializer_class = ShopProductSerializer