from django.contrib import admin
from .models import Review, Survey, Product, Answer

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class SurveyAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5']
    
class ProductAdmin(admin.ModelAdmin):
    product_display = ['image', 'name', 'category', 'menthol', 'sweet']

class AnswerAdmin(admin.ModelAdmin):
    answer_display = ['category', 'menthol', 'sweet']


admin.site.register(Review, ReviewAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Answer, AnswerAdmin)
