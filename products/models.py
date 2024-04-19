from django.conf import settings
from django.db import models


User =settings.AUTH_USER_MODEL

# Create your models here.
class Product(models.Model):
   user = models.ForeignKey(User, on_delete=models.SET_NULL , default =1 ,  null=True)
   title = models.CharField(max_length=120)
   content = models.TextField(null=True, blank=True)
   price  = models.DecimalField(decimal_places=2, max_digits=20 , default=100.00)
   
   
   @property
   def sale_price(self):
       return "%.2f"%(float(self.price) * 0.8)