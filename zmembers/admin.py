from django.contrib import admin
from .models import CustomUser, Address, Comment


admin.site.register(Address)
admin.site.register(Comment)
admin.site.register(CustomUser)