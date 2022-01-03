from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from ..models import Review, Comment
from ..forms import ReviewForm

def review_list(request):
    # 입력 param
    page = request.GET.get('page', '1') #페이지
    kw = request.GET.get('kw', '') #검색어
    so = request.GET.get('so', '') # 정렬기준
    # 정렬
    if so == 'recommend':
        review_list = Review.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        review_list = Review.objects.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    else:
        review_list = Review.objects.order_by('-create_date')
        
    # 검색
    # review_list = Review.objects.order_by('-create_date')
    if kw:
        review_list = review_list.filter(
            Q(subject__icontains=kw) | # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) | # 리뷰 글쓴이검색
            Q(comment__author__username__icontains=kw) # 댓글 글쓴이검색
        ).distinct()
    # 페이징처리
    paginator = Paginator(review_list, 15)
    page_obj = paginator.get_page(page)
    context = {'review_list': page_obj, 'page':page, 'kw':kw, 'so': so}
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
            review.author = request.user
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