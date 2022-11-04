from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from datetime import datetime, timedelta
from django.utils import timezone

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
    
    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False