from django.contrib import admin
from .models import Beranda, Produk
# Register your models here.

class BerandaAdmin(admin.ModelAdmin):
    list_display = ("nama", "keterangan",)

class ProdukAdmin(admin.ModelAdmin):
    list_display = ("nama", "keterangan",)

admin.site.register(Beranda, BerandaAdmin)
admin.site.register(Produk, ProdukAdmin)