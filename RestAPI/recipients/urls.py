from rest_framework.routers import SimpleRouter

from .views import RecipientViewSet


router = SimpleRouter()
router.register('api/v1/recipients', RecipientViewSet)

urlpatterns = router.urls