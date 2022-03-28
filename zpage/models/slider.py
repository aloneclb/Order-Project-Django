from django.db import models
from django.utils.html import mark_safe


# For Slider Delete İmage
from OrderProject.settings import BASE_DIR
from django.dispatch import receiver
from django.db.models.signals import post_delete
import os



class Slider(models.Model):
    """
        Home Page Dynamic Slider Modal
    """
    banner =            models.ImageField(
                            upload_to = 'banner/',
                            default='banner/default.png',
                            verbose_name='Banner Fotoğrafı',
                            help_text='Fotoğrafın 1296x512 Piksel Boyutunda Olması Gerekiyor') 
    title  =            models.CharField(max_length=50, blank=True, null=True)
    link   =            models.CharField(max_length=200, blank=True, null=True)
    created_time =      models.DateTimeField(auto_now_add=True) 
    update_time =       models.DateTimeField(auto_now=True)

    def banner_tag(self):
        # Admin tarafında Product Image göstermek için.
        return mark_safe('<img src="{}" height="70" width="150" />'.format(self.banner.url))

    class Meta:
        ordering = ('-created_time',)
        verbose_name_plural = "Slider Ayarları"
    
    def __str__(self):
        if self.title:
            return self.title 
        else:
            return 'Bu Slidera İsim Girilmemiştir'




@receiver(post_delete, sender = Slider)
def delete_image_slider(instance, *args, **kwargs):
    """
        Yer Kaplamamsın Diye Silinen Slider'ın İmage'inide Siliyorum
    """
    try:
        if instance.banner.url != '/media/banner/default.png':
            os.remove(str(BASE_DIR)+ str(instance.banner.url).replace('/',"\\"))
            print('dosyadan silindi.')
        else:
            print('default resim')
    
    except:
        print('Türkçe Karakter Hatası')
    