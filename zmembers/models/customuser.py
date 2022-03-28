from django.db import models
from django.conf import settings
from zmembers.choices import GenderChoices




class CustomUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Kullanıcı", on_delete=models.CASCADE)
    
    phone = models.CharField(verbose_name='Telefon Numarası',max_length=10, null=True, blank=True)
    date_birth = models.DateField(verbose_name='Doğum Tarihi', null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GenderChoices.CHOICES, null=True, blank=True)
    
    def __str__(self):
        return self.user.username +' Kullanıcı Bilgileri'