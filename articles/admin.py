from django.contrib import admin
from .models import *

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "title",
        "slug",
        "category",
        "available_display",
        "created_at",
    ]
    list_filter = [
        "available_display",
        "created_at",
        "category",
    ]

    prepopulated_fields = {"slug": ("title",)}
