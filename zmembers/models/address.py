from django.db import models
from django.conf import settings

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    invoice = models.BooleanField(default=False) # Fatura Adresimi
    name = models.CharField(verbose_name='Ad', max_length=35)
    last_name = models.CharField(verbose_name='Soyad', max_length=35)
    phone = models.CharField(verbose_name='Telefon', max_length=35)
    province = models.CharField(verbose_name='İl', max_length=35)
    district = models.CharField(verbose_name='İlçe', max_length=35)
    neighborhood = models.CharField(verbose_name='Mahalle', max_length=35)
    address_description = models.TextField(verbose_name='Adres Tarifi', max_length=255) 
    address_title = models.TextField(verbose_name='Adres Başlığı', max_length=50) 
    start_date = models.DateTimeField(auto_now_add=True) # Adres Eklenme Tarihi
    update_date = models.DateTimeField(auto_now=True) # Adres Güncellenme Tarihi
