from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import NetworkNode, Product
from .serializers import NetworkNodeSerializer, ProductSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        country = self.request.query_params.get('country')
        if country:
            return self.queryset.filter(country=country)
        return self.queryset


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
