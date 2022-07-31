from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import generics, viewsets
from .models import Order, ShopProductOrder
from .serializers import OrderSerializer, ShopProductOrderSerializer

class OrderApiView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user']

class ShopProductOrderApiView(viewsets.ModelViewSet):
    queryset = ShopProductOrder.objects.all()
    serializer_class = ShopProductOrderSerializer