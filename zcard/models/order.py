from django.db import models
from zcard.models.orderitem import OrderItem

# User Modeli İçin
from django.conf import settings


import random
import string
import itertools


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem) # Ürünler
    # İlişkisel Alanlar

    ref_code = models.CharField(max_length=12, unique=True)
    start_date = models.DateTimeField(auto_now_add=True) # Siparişin Başladığı Tarih
    update_date = models.DateTimeField(auto_now=True) # Siparişin Güncellenme Tarihi
    ordered_date = models.DateTimeField() # Siparişin Verildiği Tarih Manuel Eklenicek
    ordered = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Sepet"
        ordering = ('-update_date',)

    def __str__(self):
        return self.user.username


    def get_total(self):
        """
            Sepetteki Tüm Fiyatları Toplamı
        """
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total
    
    def save(self, *args, **kwargs):
        if not self.id: # Eğer Veritabanında daha önceden atanmış bir pk'sı yoksa
            self.ref_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))

            for x in itertools.count(1):
                if not Order.objects.filter(ref_code = self.ref_code).exists():
                    break
                self.ref_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))

        super(Order, self).save()