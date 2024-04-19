from rest_framework import serializers
from . models import Product
from rest_framework.validators import UniqueValidator


def validate_title(value):

    qs =Product.objects.filter( title__iexact = value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already taken .")
    return value

# if i need to make it unique i need to import anther model


unique_title_for_all_user = UniqueValidator(queryset = Product.objects.all() , message = "This title is already taken .")