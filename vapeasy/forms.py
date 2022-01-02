from django import forms
from vapeasy.models import Review, Comment, Survey


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [
            'answer1',
            'answer2',
            'answer3',
            'answer4',
            ]