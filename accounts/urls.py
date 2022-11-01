from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
    path("<str:username>/", views.detail, name="detail"),
    # path("update/", views.update, name="update"),
]
