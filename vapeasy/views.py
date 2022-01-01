from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def survey(request):
    return render(request, 'common/survey.html')

def review_list(request):
    page = request.GET.get('page', '1')
    review_list = Review.objects.order_by('-create_date')
    paginator = Paginator(review_list, 15)
    page_obj = paginator.get_page(page)
    context = {'review_list': page_obj}
    return render(request, 'vapeasy/review_list.html', context)

def review_datail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'vapeasy/review_detail.html', context)

@login_required(login_url='common:signin')
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

@login_required(login_url='common:signin')
def review_modify(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('vapeasy:review_detail', review_id=review.id)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.modify_date = timezone.now()
            review.save()
            return redirect('vapeasy:review_detail', review_id=review.id)
        
    else:
        form = ReviewForm(instance=review)
        context = {'form': form}
    return render(request, 'vapeasy/review_form.html', context)

@login_required(login_url='common:signin')
def review_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('vapeasy:review_detail', review_id=review.id)
    review.delete()
    return redirect('vapeasy:review_list')

@login_required(login_url='common:signin')
def comment_create_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.create_date = timezone.now()
        comment.review = review
        comment.save()
        return redirect('vapeasy:review_detail', review_id=review.id)
    else:
        form = CommentForm()
        context = {'form': form}
        return redirect('vapeasy:review_detail', review_id=review.id)

@login_required(login_url='common:login')
def comment_modify_review(request, review_id):
    comment = get_object_or_404(Review, pk=review_id)
    if request.user != comment.author:
        messages.error(request, '댓글 수정권한이 없습니다.')
        return redirect('vapeasy:review_detail', review_id=comment.review.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('vapeasy:review_detail', review_id=comment.review.id)

@login_required(login_url='common:login')
def comment_delete_review(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글 삭제권한이 없습니다')
        return redirect('vapeasy:review_detail', review_id=comment.review.id)
    else:
        comment.delete()
    return redirect('vapeasy:review_detail', review_id=comment.review.id)
