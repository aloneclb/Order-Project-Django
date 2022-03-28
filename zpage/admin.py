from django.contrib import admin
from .models import Slider, SiteSettings, Contact, AboutUs
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email', 'phone', 'status', 'note']
    list_filter = ['status',]
    readonly_fields = ['name','email', 'phone']

admin.site.register(SiteSettings)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Slider)
admin.site.register(AboutUs)


