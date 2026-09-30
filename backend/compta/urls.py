from rest_framework.routers import DefaultRouter
from .views import CompteViewSet, OperationViewSet

router = DefaultRouter()

router.register("comptes", CompteViewSet)
router.register("operations", OperationViewSet)

urlpatterns = router.urls