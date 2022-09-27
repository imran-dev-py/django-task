from rest_framework import routers
from product.viewsets import ProductViewSet, ProductVariantViewSet, ProductVariantPriceViewSet, ProductImageViewSet
router = routers.DefaultRouter()

router.register('product', ProductViewSet)
router.register('product_variant', ProductVariantViewSet)
router.register('product_variant_price', ProductVariantPriceViewSet)
router.register('product_image', ProductImageViewSet)