from django.contrib import admin
from products.models import Product
from products.models import Review
# Register your models here.
admin.site.register(
    [
        Product,
        Review
    ]
)