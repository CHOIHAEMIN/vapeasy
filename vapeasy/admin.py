from django.contrib import admin
from .models import Review, Survey

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class SurveyAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer1', 'answer2', 'answer3', 'answer4']

admin.site.register(Review, ReviewAdmin)
admin.site.register(Survey, SurveyAdmin)
