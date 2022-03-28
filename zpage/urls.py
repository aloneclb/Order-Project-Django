from django.urls import path
from . import views

urlpatterns = [   
     
    path('', views.index, name='index'), # Index Page Url
    path('hakkimizda/', views.index, name='aboutus'), # Hakkımızda Page Url
    path('iletisim/', views.contact, name='contact'),

]
