from django.db import models
from zproduct.models import Product
# User Modeli İçin
from django.conf import settings


class OrderItem(models.Model):
    user =          models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    item =          models.ForeignKey(Product, on_delete=models.CASCADE) # Sepet Ürünü
    # İlişkisel Alanlar

    quantity =      models.IntegerField(default=1) # Ürün Miktarı
    
    start_date = models.DateTimeField(auto_now_add=True) # Item Eklenme Tarihi
    update_date = models.DateTimeField(auto_now=True) # Item Güncellenme Tarihi

    class Meta:
        verbose_name_plural = "Sepete eklenen Ürünler"
        ordering = ('-update_date',)


    def __str__(self):
        return f"{self.quantity} adet {self.item.brand}{self.item.title}"

    
    def get_total_item_price(self):
        """
            Ürünün Miktarı ve fiyatı çarpımını getirir.
        """
        return (self.item.discount_price * self.quantity)
    

    def reduce_to_quantity(self):
        """
            İtem miktarı azaltma ve 0'dan küçükse sepetten silme
        """
        self.quantity -=1
        
        if self.quantity <= 0:
            super(OrderItem, self).delete()
        else:
            super(OrderItem, self).save() 



