from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet


router = DefaultRouter()
router.register('products-111', ProductViewSet , basename= 'products')

# print(router.urls)
urlpatterns = [router.urls ]  # This is a list of urls that we can include in our urls.py file validators