from django.contrib import admin
from .models import Product  # Only Product, no Category

# Register Product model to appear in Django admin
admin.site.register(Product)
