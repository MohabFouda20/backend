from . models import Product
from rest_framework import generics ,mixins , permissions , authentication
from .serializers import productSerializer
# from ..api.permissions import IsStaffEditorPermission
from api.permissions import IsStaffEditor
from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin ,UserQuerySetMixin


#for the function based views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

 
#class mixins views
# class productMixinView(
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    # mixins.CreateModelMixin,
    # mixins.ListModelMixin,
    # mixins.RetrieveModelMixin,
    # generics.GenericAPIView
    # ):
    # queryset = Product.objects.all()
    # serializer_class  = productSerializer
    # lookup_field = 'pk'
    
    # def get (self , request , pk = None , *args, **kwargs):
    #     pk  = kwargs.get("pk")
    #     if pk is not None:
    #         return self.retrieve(request, *args, **kwargs)
    #     return self.list(request , *args , **kwargs)
    
    # def post(self , request , *args , **kwargs):
    #     return self.create(request , *args , **kwargs)
    
    
    
    # def put(self , request , *args, **kwargs):
    #     # instance_pk = kwargs.get(self.lookup_field)
    #     return self.update(request , *args , **kwargs)
    
    # def delete(self , request , *args, **kwargs):
    #     # pk = kwargs.get('pk')
    #     return self.destroy(request , *args , **kwargs)
    
    
# product_Mixin_View = productMixinView.as_view() # this is a class based view



#---------------------------------------------------------------------------------------------------------------------------------


# class generic api views 
class productListCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView ,UserQuerySetMixin):
    queryset  = Product.objects.all()
    serializer_class = productSerializer
    
    # permission_classes = [ permissions.IsAdminUser, IsStaffEditor]
    
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     TokenAuthentication,                      we changed it with the defult one in setting.py
    #     ]




    def preform_create(self , serializer):
        print (serializer.validated_data)
        serializer.save()
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content= title
        serializer.save(user = self.request.user , content=content)
        
        
        
    # def get_queryset(self , *args, **kwargs):
    #     qs  = super().get_queryset( *args, **kwargs)
    #     request = self.request
    #     # print (request.user) 
    #     return qs.filter(user = request.user)
    
ProductListCreateView = productListCreateApiView.as_view()



class productDetailAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    
    queryset = Product.objects.all()
    serializer_class = productSerializer
    
    
    
ProductDetail_view = productDetailAPIView.as_view() # this is a class based view 


class productUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'
    
    def preformUpdate(self , serializer):
        instance =serializer.save()
        if instance.content is None:
            instance.content = instance.title
            instance.save()
    
ProductUpdateView = productUpdateAPIView.as_view() # this is a class based view 


class productDeleteAPIView(StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    
    def preformDelete(self , instance):
        super().preformDelete(instance)
    
    
    
ProductDeleteView = productDeleteAPIView.as_view() # this is a class based view



#---------------------------------------------------------------------------------------------------------------------------------

# fuction based view
# @api_view(['GET' , 'POST'])
# def prouduct_alt_view(request , pk = None,*args, **kwargs):
    # method = request.method 
    # if method =='GET':
    #     if pk is not None:
    #         obj = get_object_or_404(Product , pk = pk)
    #         data = productSerializer(obj , many = False).data
    #         return Response(data)
    #     qs = Product.objects.all()
    #     data = productSerializer(qs , many = True).data
    #     return Response(data)
    
    # if method == 'POST':
    #     serializer = productSerializer(data = request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         title = serializer.validated_data.get('title')
    #         content = serializer.validated_data.get('content') or None
    #         if content is None:
    #             content = title
    #         serializer.save(content=content)
    #         return Response(serializer.data)