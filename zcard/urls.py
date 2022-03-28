from django.urls import path
from . import views

app_name = 'card'

urlpatterns = [    
    path('summary/', views.order_summary, name='order_summary'), # Sipariş Özeti,

    path("product/add/<slug:barcode>/<slug:slug>/", views.add_to_cart, name="add_to_cart"), # Karta Ekleme
    
    path("product/remove/<slug:barcode>/<slug:slug>/", views.remove_to_cart, name="remove_to_cart"), # Karttan Çıkarma

    path("product/delete/<slug:barcode>/<slug:slug>/", views.delete_to_cart, name='delete_to_cart' ),# Karttan Eksiltme

    path('checkout/', views.checkout, name='checkout')

]
