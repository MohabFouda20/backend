from django.urls import path
from . import views




urlpatterns = [
    
    # mixins based view
     
    # path('',views.product_Mixin_View),
    # path('<int:pk>/',views.product_Mixin_View),
    # path('<int:pk>/update/',views.product_Mixin_View),
    # path('<int:pk>/delete/',views.product_Mixin_View),
    
    
 #---------------------------------------------------------------------------------------------------------------------------------
    #generic based view
    
    
    path('',views.ProductListCreateView , name = 'product_list'),
    path('<int:pk>/',views.ProductDetail_view , name = 'product_detail'),
    path('<int:pk>/update',views.ProductUpdateView , name='product_edit'),
    path('<int:pk>/delete',views.ProductDeleteView , name = 'product_delete'),
    
    
 #---------------------------------------------------------------------------------------------------------------------------------
    
    # function based view
    # path('',views.prouduct_alt_view),
    # path('<int:pk>/',views.prouduct_alt_view),
]
