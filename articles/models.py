from django.db import models
from django.db import models
from django.conf import settings

# Create your models here.
class Tag(models.Model):
    name = models.CharField("태그명", max_length=255, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
    )
    image = models.ImageField(upload_to="images/", blank=True)
    tags = models.ManyToManyField(Tag, verbose_name="태그", blank=True)

    hits = models.PositiveIntegerField(default=0)

    @property
    def click(self):
        self.hits += 1
        self.save()

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
