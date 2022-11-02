from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.hashers import check_password

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)
        labels = {
            "username": "아이디",
        }

class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "first_name",
            "last_name",
        )

class CheckPasswordForm(forms.Form):
    password = forms.CharField(widget = forms.PasswordInput())
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password
        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 달라요.')