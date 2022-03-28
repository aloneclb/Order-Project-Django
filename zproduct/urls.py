from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [    
    path('', views.product_list, name='product_list'), # Product list
    path('category/<slug:slug>', views.category_list, name='category_list'), # Category List
    path('search/', views.product_search, name='product_search'), # Search List
    # path('search/<slug:query>', views.product_search, name='product_search'), # Search List

    path('<slug:slug>/<slug:barcode>', views.product_detail, name='product_detail'), # Product Detail
    path('filter/', views.product_filter, name='product_filter'), # Product Detail

]
