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
    
    # 물음내용 1~4
    answer1 = models.CharField(max_length=50, null=True, blank=True)
    answer2 = models.CharField(max_length=50, null=True, blank=True)
    answer3 = models.CharField(max_length=50, null=True, blank=True)
    answer4 = models.CharField(max_length=50, null=True, blank=True)

class Answer(models.Model):
    # 설문조사 물음내용마다 연결하기 위한 외래키
    # survey = models.ForeignKey(Survey, null=True, blank=True, on_delete=models.CASCADE)
    
    # 선택옵션중 택1 했을때 저장하기 위한 속성
    choice = models.CharField(max_length=50, null=True, blank=True)
    
    # 어느 회원의 답변인지 확인 위한 속성
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Product(models.Model):
    image = models.ImageField(blank=True, upload_to="")
    name = models.CharField(max_length=50)
    sort1 = models.CharField(max_length=50)
    sort2 = models.CharField(max_length=50)
    detail = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name


# 업로드한 이미지파일 사용하는 방법
# {% if profile.photo %}

# <img src="{{ profile.photo.url }}" >
# or
# <img src="{{ profile.photo.path }}" >
# or
# <img src="{{ article.image.url }}" alt="{{ article.image }}">
#               업로드 파일의 경로         업로드 파일의 파일 이름

# {% endif %}













