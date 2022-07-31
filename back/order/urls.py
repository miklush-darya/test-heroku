from django.urls import path, include
from django.conf.urls.static import static
from .views import OrderApiView, ShopProductOrderApiView
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api/order', OrderApiView, 'order')
router.register('api/orderproducts', ShopProductOrderApiView, 'orderproducts')

urlpatterns = router.urls