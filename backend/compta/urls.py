from rest_framework.routers import DefaultRouter

from .views import (
    CompteViewSet,
    OperationViewSet,
)


router = DefaultRouter()

router.register(
    "comptes",
    CompteViewSet,
    basename="compte"
)

router.register(
    "operations",
    OperationViewSet,
    basename="operation"
)

urlpatterns = router.urls