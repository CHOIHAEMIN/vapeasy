from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')
    create_date = models.DateTimeField()
    def __str__(self):
        return self.subject