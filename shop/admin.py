from django.contrib import admin
from.import models
# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.Contact)
admin.site.register(models.Orders)
admin.site.register(models.OrderUpdate)

# from .models import Product, Contact