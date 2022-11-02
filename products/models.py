from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

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
    review_image = ProcessedImageField(
		upload_to = 'media/',
		processors = [Thumbnail(300, 300)], # 처리할 작업 목룍
		format = 'JPEG',					# 최종 저장 포맷
		options = {'quality': 60})
    # 내구성
    grade_durability = models.FloatField()
    # 가격
    grade_price = models.FloatField()
    # 디자인
    grade_design = models.FloatField()
    # 실용성
    grade_practicality = models.FloatField()
    grade_avg = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews")