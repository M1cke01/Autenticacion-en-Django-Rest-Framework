from rest_framework import serializers
from forms_test.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["user", "title", "price", "slug"]