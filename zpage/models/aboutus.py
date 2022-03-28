from django.db import models

# For Ck Editor 
from ckeditor_uploader.fields import RichTextUploadingField

# Status
from zpage.choices import StatusChoices

# For AboutUs Modal-Slug
from django.template.defaultfilters import slugify
import itertools





class AboutUs(models.Model):
    title =             models.CharField(max_length=250)
    description =       RichTextUploadingField(blank=True, null=True)
    status =            models.PositiveIntegerField(choices=StatusChoices.CHOICES) # Choices Alanı Oluşturduk
    created_time =      models.DateTimeField(auto_now_add=True) 
    update_time =       models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Hakkımızda Ayarları"
        ordering = ('-update_time',)
        

    def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
        """
            Kaydederken Status'ü Silmekse Silme işlemini yapar
        """
        # Choices Değerini 2 olunca delete işlemi istiyor demektir.
        if self.status == 2:
            super(AboutUs, self).delete()
        super(AboutUs, self).save()





