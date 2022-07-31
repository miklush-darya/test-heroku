from django.urls import path, include
from django.conf.urls.static import static
from user.views import ShopApiView, UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()

# router.register('api/user', UserApiView.as_view({'get': 'list'}), 'user')
router.register('api/users', UserViewSet, 'users')
router.register('api/shop', ShopApiView, 'shop')

urlpatterns = router.urls
