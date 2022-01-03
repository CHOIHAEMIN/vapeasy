from django.shortcuts import get_object_or_404, redirect, resolve_url
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import Review, Comment
from ..forms import CommentForm
# Create your views here.

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
        return redirect('{}#answer_{}'.format(resolve_url('vapeasy:review_detail', review_id=review_id), comment.id))
    else:
        form = CommentForm()
        context = {'form': form}
        return redirect('vapeasy:review_detail', review_id=review.id)

@login_required(login_url='common:signin')
def comment_modify_review(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
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
            return redirect('{}#comment_{}'.format(resolve_url('vapeasy:review_detail', review_id=comment.review.id), comment.id))

@login_required(login_url='common:signin')
def comment_delete_review(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글 삭제권한이 없습니다')
        return redirect('vapeasy:review_detail', review_id=comment.review.id)
    else:
        comment.delete()
    return redirect('vapeasy:review_detail', review_id=comment.review.id)
