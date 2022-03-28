from django.db import models
from .product import Product

# Signal Delete İmage
from OrderProject.settings import BASE_DIR
from django.dispatch import receiver
from django.db.models.signals import post_delete
import os



class Images(models.Model):
    #İlişkisel alanlar
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=130, verbose_name='Fotoğraf Adı')
    image = models.ImageField(upload_to = 'product/%Y/%m/%d/', default='product/default.png', help_text='1200x1200 piksel fotoğraf olmalıdır.') 
    created_time = models.DateTimeField(auto_now_add=True) 
    update_time = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.title
    
    

@receiver(post_delete, sender = Images)
def delete_image_product(instance, *args, **kwargs):
    """
        Yer Kaplamamsın Diye Silinen Product'ın Frontİmage'inide Siliyorum
    """
    try:
        if instance.image.url != '/media/product/default.png':
            os.remove(str(BASE_DIR)+ str(instance.image.url).replace('/',"\\"))
            print('dosyadan silindi.')
        else:
            print('default resim')
    except:
        print('Hata')