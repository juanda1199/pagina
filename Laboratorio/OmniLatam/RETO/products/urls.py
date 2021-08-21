from rest_framework import routers
from .views import ProductViewSet

router = routers.SimpleRouter()
router.register('product', ProductViewSet, basename='product')
urlpatterns = router.urls
