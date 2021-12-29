from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Review
from .forms import ReviewForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def survey(request):
    return render(request, 'common/survey.html')

def review_list(request):
    review_list = Review.objects.order_by('-create_date')
    context = {'review_list': review_list}
    return render(request, 'vapeasy/review_list.html', context)

def review_datail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'vapeasy/portfolio_review_detail.html', context)

def review_create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            # review.author = request.user
            review.create_date = timezone.now()
            review.save()
            return redirect('vapeasy:review_list')
    else:
        form = ReviewForm()
    return render(request, 'vapeasy/review_form.html', {'form': form})