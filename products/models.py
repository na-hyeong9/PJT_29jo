from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    product_image = models.ImageField()
    price = models.IntegerField()
    product_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "like_products")

class Review(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    review_image = models.ImageField(blank=True)
    grade_1 = models.FloatField()
    grade_2 = models.FloatField()
    grade_3 = models.FloatField()
    grade_4 = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews")
    