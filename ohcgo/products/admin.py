from django.contrib import admin

from ohcgo.products import models

class ProductAdmin(admin.ModelAdmin):
    """
    Make products editable
    """
    list_display = ('name', 'frontpage', 'featured', 'category')
    list_editable = ('frontpage', 'featured', 'category')
    list_filter = ('category',)
    save_as = True

admin.site.register(models.Product, ProductAdmin)
