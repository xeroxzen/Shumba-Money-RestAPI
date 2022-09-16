from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CustomerViewSet, UserViewSet


router = SimpleRouter()
router.register('customers', CustomerViewSet, basename='customers')
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls