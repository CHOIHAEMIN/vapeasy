from django import forms
from vapeasy.models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review

        fields = ['subject', 'content']

        widgets = {
        'subject': forms.TextInput(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }

        labels = {
            'subject' : '제목',
            'content' : '내용'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']