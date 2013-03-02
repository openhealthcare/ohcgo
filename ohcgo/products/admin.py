from django.contrib import admin

from ohcgo.products import models

class ProductAdmin(admin.ModelAdmin):
    """
    Make products editable
    """
    list_display = ('name', 'description', 'image_location', 'category')
    list_editable = ('description', 'image_location', 'category')
    list_filter = ('category',)

admin.site.register(models.Product, ProductAdmin)
