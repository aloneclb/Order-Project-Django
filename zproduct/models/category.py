from django.db import models
from zproduct.choices import StatusChoices
from django.template.defaultfilters import slugify
import itertools


class Category(models.Model):
    # İlişkisel Alanlar
    title = models.CharField(max_length=30, verbose_name='Kategori Adı')
    status = models.PositiveIntegerField(choices=StatusChoices.CHOICES, verbose_name='Kategori Durumu') # Choices Alanı Oluşturduk
    slug = models.SlugField(unique=True, editable=False) # Slug'ı Otomatik Olarak Oluşturucaz
    created_time = models.DateTimeField(auto_now_add=True) 
    update_time = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """
            models.Model.save() metodu çalışırken eşsiz bir slug yaratma
        """
        if not self.id: # Eğer Veritabanında daha önceden atanmış bir pk'sı yoksa
            self.slug = slugify(self.title)

            for slug_id in itertools.count(1):
                if not Category.objects.filter(slug = self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, slug_id)
        super(Category, self).save()

        # ----------------- Status'e Göre Silme İşlemi ---------------------
        # Choices Değerini 2 olunca delete işlemi istiyor demektir.
        if self.status == 2:
            super(Category, self).delete()