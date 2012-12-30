from django.contrib import admin

from ohcgo.products import models

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Product

admin.site.register(models.Product, ProductAdmin)
