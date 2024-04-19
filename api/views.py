import json
from django.shortcuts import render
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import productSerializer
from django.http import JsonResponse
# Create your views here.

@api_view(["POST"])
def api_home(request , *args, **kwargs):
    """"
    DRF view
    """
    serializer = productSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        instance= serializer.save()
        print (instance)
        return Response(serializer.data)


# @api_view(['GET'] ) # only get request is allowed
# def api_home (request ,*args, **kwargs):
    # """
    # now it will be DRF view

    # """
    # instance = Product.objects.all().order_by('?').first()
    # data = {}
    # if instance:
    #     # data = {
    #     #     "id" : model_data.id,
    #     #     "title" : model_data.title,
    #     #     "content" : model_data.content,
    #     #     "price" : model_data.price
    #     # } or we can use model_to_dict
        
    #     # data = model_to_dict(model_data , fields = [ 'title' , 'price'])
    #     data = productSerializer(instance).data
    # return Response(data) # get the response in form of html

# def api_home (request ,*args, **kwargs):
    print (request.GET) #print the query parameters  ->    <QueryDict: {'abs': ['123']}> in case of params ={'abs' : 123}
    body = request.body
    data = {}
    try:
        data = json.loads(body) # json data -> python dictionary    ->    {'query': 'hello world'}
    except:
        pass
    print (data)
    return JsonResponse(data) # get the response in form of html