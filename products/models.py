from django.conf import settings
from django.db import models
from django.db.models import Q


User =settings.AUTH_USER_MODEL

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    
    def search(self , query , user =None):
        lookup = (Q(title__icontains = query) | Q(content__icontains = query))
        qs  =  self.is_public().filter(lookup)
        if user is not None :
            qs2 = self.filter(user = user).filter(lookup)
            qs = (qs | qs2).distinct()
            # return qs.filter(user = user)
        return qs

class ProductManager(models.Manager):
    def get_queryset(self , *args, **kwargs):
        return ProductQuerySet(self.model , using=self._db)
        
        
        
    def search (self , query , user =None):
        return self.get_queryset().search(query , user=user)

# Create your models here.
class Product(models.Model):
   user = models.ForeignKey(User, on_delete=models.SET_NULL , default =1 ,  null=True)
   title = models.CharField(max_length=120)
   content = models.TextField(null=True, blank=True)
   price  = models.DecimalField(decimal_places=2, max_digits=20 , default=100.00)
   public=  models.BooleanField(default=True)
   objects= ProductManager()
   
   @property
   def body(self):
        return self.content
   @property
   def sale_price(self):
       return "%.2f"%(float(self.price) * 0.8)