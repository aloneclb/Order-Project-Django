from django.db import models


# Kullanıcıların İletişim Formlarını Saklamak İçin Model
class Contact(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('Read', 'Okundu'),
        ('Important','Önemli'),
        ('Close', 'Cevap Verildi')
    )
    name =       models.CharField(max_length=30)
    email =      models.CharField(max_length=50)
    message =    models.TextField(blank=True, max_length=255)
    phone =      models.CharField(max_length=50)
    ip =         models.CharField(max_length=50, default='Ip Belirtilmedi')
    status =     models.CharField(max_length=10, choices=STATUS, default='New')
    note =       models.CharField(max_length=70,verbose_name='Admin Notu', default='Not Alınmadı')
    created_time = models.DateTimeField(auto_now_add=True) 
    update_time =  models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name