from django.contrib import admin
from zproduct.models import Category, Product, Images, Wishlist

# Register your models here.


# Inlines
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 3



# Product Model
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'brand', 'title', 'category', 'image_tag', 'price', 'stock']
    list_filter = ['category']
    list_display_links = ('pk', 'brand', 'title')
    inlines = [ProductImageInline]






admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)
admin.site.register(Wishlist)






