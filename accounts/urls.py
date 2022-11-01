from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("<str:username>/", views.detail, name="detail"),
    path("<int:pk>/follow/", views.follow, name="follow"),
    # path("update/", views.update, name="update"),
]
