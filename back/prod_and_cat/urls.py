from django.urls import path, include
from django.conf.urls.static import static
from prod_and_cat.views import CategoryApiView, ProductViewSet, ShopProductApiView
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api/category', CategoryApiView, 'category')
router.register('api/products', ProductViewSet, 'products')
# router.register('api/products/addproduct', ProductViewSet, 'addproduct')
# router.register('api/products/create', ProductAPIView, 'productscr') ##########
router.register('api/shopproducts', ShopProductApiView, 'shopproducts')

urlpatterns = router.urls
