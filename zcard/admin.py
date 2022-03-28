from django.contrib import admin
from .models import OrderItem, Order

# Product Model
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['pk', '__str__', 'item', 'user', 'quantity', 'get_total_item_price']
    list_display_links = ('pk', '__str__', 'item')





admin.site.register(Order)
admin.site.register(OrderItem, OrderItemAdmin)
