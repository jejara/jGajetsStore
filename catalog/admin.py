from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Brand)
admin.site.register(models.CartItem)
admin.site.register(models.Cart)
