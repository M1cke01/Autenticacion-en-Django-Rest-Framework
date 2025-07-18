from django.shortcuts import render
from rest_framework import generics
from .pagination import ProductPagination, ProductLOPagination, ProductCPagination
from .serializers import ProductSerializer
from forms_test.models import Product

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # pagination_class = ProductPagination
    # pagination_class = ProductLOPagination
    pagination_class = ProductCPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

