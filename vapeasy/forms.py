from django import forms
from vapeasy.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'content']