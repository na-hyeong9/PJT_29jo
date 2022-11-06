from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("my_cart/", views.my_cart, name="my_cart"),
    path("add_cart/<int:product_id>", views.add_cart, name="add_cart"),
]
