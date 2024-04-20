from django.urls import path
from . import views

urlpatterns = [
    path('', views.searchListAPIView.as_view(), name='query'),
    
    
    ]
