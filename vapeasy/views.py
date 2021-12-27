from django.shortcuts import render
from django.http import HttpResponse
from .models import Review
# Create your views here.

def index(request):
    review_list = Review.objects.order_by('-create_date')
    context = {'review_list': review_list}
    return render(request, 'vapeasy/portfolio_review_list.html', context)