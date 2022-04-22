from django.shortcuts import render
# Create your views here.

def index(request):
    3/0 #오류 발생
    return render(request, 'index.html')

# def survey(request):
#     return render(request, 'common/survey.html')

