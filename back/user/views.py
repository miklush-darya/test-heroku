from django.shortcuts import render
from rest_framework import generics, viewsets, status, filters, mixins, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Shop
from .serializers import UserSerializer, ShopSerializer, RegisterSerializer


# Create your views here.


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = User.objects
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes_by_action = {
        "create": [permissions.AllowAny,],
    }

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_permissions(self):
        if self.action in self.permission_classes_by_action:
            permissions = self.permission_classes_by_action[self.action]
        else:
            permissions = self.permission_classes
        return [permission() for permission in permissions]


    def get_serializer_class(self):
    
        if self.action == "create":
            return RegisterSerializer

        return self.serializer_class

    @action(methods=['GET'], detail=False)
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)



class ShopApiView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

