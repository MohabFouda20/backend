from rest_framework import generics
from products.models import Product
from products.serializers import productSerializer

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