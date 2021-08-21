from rest_framework import routers
from .views import UserViewSet, NotificationViewSet
from django.urls import path, include

router = routers.SimpleRouter()
router.register('user', UserViewSet,)
router.register('notification', NotificationViewSet, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]
