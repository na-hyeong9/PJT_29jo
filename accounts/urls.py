from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # path("<str:username>/", views.detail, name="detail"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    # path("update/", views.update, name="update"),
    # path("<int:user_id>/follow/", views.follow, name="follow"),
]
