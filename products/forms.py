from django import forms
from .models import Review

class ReviewCreationForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content', 'review_image',)