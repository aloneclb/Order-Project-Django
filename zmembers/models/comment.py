from django.db import models
from django.conf import settings
from zproduct.models import Product



class Comment(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('Read', 'Okundu'),
        ('Close', 'Cevap Verildi')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Kullanıcı", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Ürün Adı", on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete= models.CASCADE, null=True, blank=True, related_name='replies') # Cevap Vermek İçin

    body = models.TextField(verbose_name='Mesaj İçeriği')
    rate = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    active = models.BooleanField(default=True)
    ip = models.CharField(blank=True, max_length=45)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return 'Comment by {} - {} '.format(self.user.username , self.product.title)