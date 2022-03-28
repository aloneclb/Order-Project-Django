from django.db import models
from .category import Category
from zproduct.choices import ProductGenderChoices

# CkEditor
from ckeditor_uploader.fields import RichTextUploadingField

# Admin Tarafında İmage Göstermek İçin Html Koduna Güven Fonksiyonu
from django.utils.html import mark_safe

# Slug Kısmı İçin
from django.template.defaultfilters import slugify
import itertools

# get_absolute_url
from django.urls import reverse


# Signal Delete İmage
from OrderProject.settings import BASE_DIR
from django.dispatch import receiver
from django.db.models.signals import post_delete
import os




class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    brand =             models.CharField(max_length=90, verbose_name='Marka')
    title =             models.CharField(max_length=100, verbose_name='Ürün Adı')
    barcode =           models.CharField(unique=True, max_length=20, verbose_name='Barkod')
    gender =            models.PositiveIntegerField(verbose_name='Cinsiyet', choices=ProductGenderChoices.CHOICES, default=0)
    price =             models.FloatField(verbose_name='Ürün Fiyatı')
    discount_price =    models.FloatField(blank=True, null=True, verbose_name='İndirimli Fiyatı')
    stock =             models.IntegerField(default=1)
    slug =              models.SlugField(unique=True, editable=False)
    description =       RichTextUploadingField(verbose_name='Ürün Detayları')
    front_image =       models.ImageField(upload_to = 'productfront/%Y/%m/%d/', 
                                            default='product/default.png', 
                                            verbose_name='Kapak Fotoğrafı',
                                            help_text = '372 x 431 Piksel Fotoğraf Olmalıdır.')

    start_date = models.DateTimeField(auto_now_add=True) # Ürünün Eklenme Tarihi
    update_date = models.DateTimeField(auto_now=True) # Ürün Güncelleme Tarihi
    

    class Meta:
        verbose_name_plural = "Ürün İşlemleri"
        ordering = ('-update_date',)

    
    def __str__(self):
        return self.title


    def image_tag(self):
        # Admin tarafında Product Image göstermek için.
        return mark_safe('<img src="{}" height="50" width="50" />'.format(self.front_image.url))



    def get_absolute_url(self):
        return reverse("product:product_detail", kwargs={
            "slug": self.slug,
            "barcode": self.barcode,
            })
    


    # Ürün Karta Ekleme URL'i
    def get_add_to_cart_url(self):
        return reverse("product:add_to_cart", kwargs={
            "barcode": self.barcode,
            "slug": self.slug,
            })
    

    def save(self, *args, **kwargs):
        """
            models.Model.save() metodu çalışırken eşsiz bir slug yaratma
        """
        # TODO: Ürünün adı değiştirildiğinde Slugı Değiştir.
        if not self.id: # Eğer Veritabanında daha önceden atanmış bir pk'sı yoksa
            self.slug = slugify(self.title)

            for slug_id in itertools.count(1):
                if not Product.objects.filter(slug = self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, slug_id)
        super(Product, self).save()






@receiver(post_delete, sender = Product)
def delete_image_product(instance, *args, **kwargs):
    """
        Yer Kaplamamsın Diye Silinen Product'ın Frontİmage'inide Siliyorum
    """
    try: # Türkçe Karakter Var ise
        if instance.front_image.url != '/media/product/default.png':
            os.remove(str(BASE_DIR)+ str(instance.front_image.url).replace('/',"\\"))
            print('dosyadan silindi.')
        else:
            print('default resim')
    except:
        print('Hata')