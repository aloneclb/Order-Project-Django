from django.db import models
from .product import Product
from django.conf import settings

class Wishlist(models.Model):
    """
        Hangi Ürünü Hangi Kullanıcı Wishlistine Eklemiş 
        Görmek için bir model.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + "  " + self.product.title
