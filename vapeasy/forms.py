from django import forms
from vapeasy.models import Review, Comment, Survey, Answer, Product


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
            'answer5',
            ]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        # fields = ['category', 'menthol', 'sweet']
        fields = ['choice']
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'category', 'menthol', 'sweet']
