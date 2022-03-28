from django.db import models
from zpage.choices import StatusChoices

# Genel Site Ayarları İçin Model
class SiteSettings(models.Model):
    title =             models.CharField(blank=True, null=True, max_length=50)
    site_welcome =      models.CharField(blank=True, null=True, max_length=50)
    keywords =          models.CharField(blank=True, null=True, max_length=255)
    description =       models.CharField(blank=True, null=True, max_length=255)
    company =           models.CharField(blank=True, null=True, max_length=50)
    address =           models.TextField(blank=True, null=True, max_length=150)
    phone =             models.CharField(blank=True, null=True, max_length=150)
    fax =               models.CharField(blank=True, null=True, max_length=50)
    email =             models.CharField(blank=True, null=True, max_length=60)
    smtpserver =        models.CharField(blank=True, null=True, max_length=50)
    smtpemail =         models.CharField(blank=True, null=True, max_length=50)
    smtppassword =      models.CharField(blank=True, null=True, max_length=50)
    smtpport =          models.CharField(blank=True, null=True, max_length=9)
    icon =              models.ImageField(upload_to ='SiteIcon/%Y/%m/%d/', blank=True)
    facebook =          models.CharField(blank=True, null=True, max_length=255)
    instagram =         models.CharField(blank=True, null=True, max_length=255)
    twitter =           models.CharField(blank=True, null=True, max_length=255)
    references =        models.CharField(blank=True, null=True, max_length=255)
    status =            models.PositiveIntegerField(choices=StatusChoices.CHOICES) # Site Durumu İçin Alanı Oluşturduk
    created_time =      models.DateTimeField(auto_now_add=True) 
    update_time =       models.DateTimeField(auto_now=True) 


    def __str__(self):
        return self.title