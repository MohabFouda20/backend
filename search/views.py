from rest_framework import generics
from products.models import Product
from products.serializers import productSerializer
from rest_framework.response import Response
from . import client

class seachNewAPIView(generics.ListAPIView):
    def get(self , request , *args, **kwargs):
        query = request.GET.get('q')
        if not query:
            return Response([])
        result = client.perform_search(query)
        return Response(result)

class searchListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    def get_queryset(self , *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        user= None
        result = Product.objects.none()
        if q is not None:
            if  self.request.user.is_authenticated:
                user = self.request.user
            result = qs.search(q , user=user)
        return result