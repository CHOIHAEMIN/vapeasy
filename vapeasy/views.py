from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Review
# Create your views here.

def index(request):
    return render(request, 'vapeasy/portfolio_main.html')

def review_list(request):
    review_list = Review.objects.order_by('-create_date')
    context = {'review_list': review_list}
    return render(request, 'vapeasy/portfolio_review_list.html', context)

def review_datail(request,review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'vapeasy/portfolio_review_detail.html', context)