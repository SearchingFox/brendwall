from django.views.generic import TemplateView
from rest_framework import generics
from .models import Product
from .serializers import ProductListSerializer, ProductCreateSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer


class IndexView(TemplateView):
    template_name = 'index.html'