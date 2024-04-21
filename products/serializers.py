from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators
from api.serializers import UserPublicSerializer


class productSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only = True)
    edit_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name = 'product_detail' , lookup_field = 'pk')
    title =serializers.CharField(validators = [validators.validate_title , validators.unique_title_for_all_user])
    body = serializers.CharField(source = 'content')

    class Meta:
        model = Product
        fields = [
            'user',
            'id',
            'title',
            'body', 
            'price',
            'sale_price',
            'url',  
            'edit_url',
            'public',
            

            ]
        
        
        
    # def get_my_user_data(self , obj):
    #     return {"username": obj.user}
    
    
    
    #can use a external function to validate the title    
    
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact = value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already taken .")
    #     return value
    
    
    
    # def create(self , validated_data):
    #     obj = super().create(validated_data)
    #     return obj
    # def update (self , instance , validated_data):
    #     obj = super().update(instance , validated_data)
    #     return obj
    
    def get_edit_url (self , obj):
        request = self.context.get("request")
        if request is None:
            return None 
        return reverse('product_edit', kwargs = {"pk": obj.pk}, request = request)