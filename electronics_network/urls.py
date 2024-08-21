from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NetworkNodeViewSet, ProductViewSet
from .apps import ElectronicsNetworkConfig


app_name = ElectronicsNetworkConfig.name


router = DefaultRouter()
router.register(r"network_nodes", NetworkNodeViewSet)
router.register(r"products", ProductViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
