from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_review')
    def __str__(self):
        return self.subject
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    review = models.ForeignKey(Review, null=True, blank=True, on_delete=models.CASCADE)
    voter = models.ManyToManyField(User, related_name='voter_comment')

class Survey(models.Model):
    # 설문조사 물음내용
    question = models.TextField(null=True)
    
    # 응답1~4
    answer1 = models.TextField(null=True)
    answer2 = models.TextField(null=True)
    answer3 = models.TextField(null=True)
    answer4 = models.TextField(null=True)