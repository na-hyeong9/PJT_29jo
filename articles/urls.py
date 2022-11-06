from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("", views.index, name="index"),
    path("<int:pk>/<article_slug>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/<article_slug>/delete/", views.delete, name="delete"),
    path("<int:pk>/comment_create/", views.comment_create, name="comment_create"),
    path("<int:pk>/comment_update/", views.comment_update, name="comment_update"),
    path(
        "<int:article_pk>/comments/<int:comment_pk>/delete/",
        views.comments_delete,
        name="comments_delete",
    ),
    path("<int:pk>/like/", views.like, name="like"),
    path("list/", views.article_in_category, name="article_all"),
    path(
        "<category_slug>",
        views.article_in_category,
        name="article_in_category",
    ),
]
