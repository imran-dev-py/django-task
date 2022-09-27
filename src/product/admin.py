from django.contrib import admin
from product import models

@admin.register(models.Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    

admin.site.register(models.Product)
admin.site.register(models.ProductImage)
admin.site.register(models.ProductVariant)
admin.site.register(models.ProductVariantPrice)