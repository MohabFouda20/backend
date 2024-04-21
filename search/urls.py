from django.urls import path
from . import views

urlpatterns = [
    path('', views.seachNewAPIView.as_view()),
    
    
    ]
