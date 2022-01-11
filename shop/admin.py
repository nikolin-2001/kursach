from django.contrib import admin

from .models import Product, Purchase, Systemunit, Accessories, Noteboo, Open

admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Systemunit)
admin.site.register(Accessories)
admin.site.register(Noteboo)
admin.site.register(Open)