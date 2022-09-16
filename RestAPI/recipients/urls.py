from rest_framework.routers import SimpleRouter

from .views import RecipientViewSet


router = SimpleRouter()
router.register('recipients', RecipientViewSet, basename='recipients')

urlpatterns = router.urls