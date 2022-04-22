from django.shortcuts import render
import logging
logger = logging.getLogger('vapeasy')
# Create your views here.

def index(request):
    logger.info("INFO 레벨로 출력")
    return render(request, 'index.html')

# def survey(request):
#     return render(request, 'common/survey.html')

