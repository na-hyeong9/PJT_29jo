from datetime import datetime, timezone, timedelta
from django.urls import reverse
from django.db import models
from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(
        max_length=20, db_index=True, unique=True, allow_unicode=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("articles:article_in_category", args=[self.slug])


class Article(models.Model):

    title = models.CharField(
        max_length=20,
        db_index=True,
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
    )
    image = models.ImageField(
        upload_to="images/%Y/%m/%d",
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="articles",
    )
    slug = models.SlugField(
        max_length=20,
        db_index=True,
        unique=True,
        allow_unicode=True,
        null=True,
    )
    available_display = models.BooleanField("Display", default=True)
    meta_description = models.TextField(blank=True)

    hits = models.PositiveIntegerField(default=0)

    class Mata:
        orderging = ["-created_at"]
        index_together = [["id", "slug"]]

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + "일 전"
        else:
            return False

    @property
    def click(self):
        self.hits += 1
        self.save()

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:detail", args=[self.pk, self.slug])


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created.date()
            return str(time.days) + "일 전"
        else:
            return False
