from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("delete/", views.delete, name="delete"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
    path("edit/", views.edit, name="edit"),
    path("<str:username>/", views.detail, name="detail"),
]
