from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:product_pk>/", views.detail, name="detail"),
    path("<int:product_pk>/reviews/create/", views.reviews_create, name="reviews_create"),
    path("<int:product_pk>/update/<int:review_pk>", views.reviews_update, name="reviews_update"),
    path("<int:product_pk>/delete/<int:review_pk>", views.reviews_delete, name="reviews_delete"),
    path("<int:product_pk>/likes/<int:review_pk>", views.reviews_likes, name="reviews_likes"),
]
