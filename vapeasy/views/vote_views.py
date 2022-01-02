from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from ..models import Review, Comment

@login_required(login_url='common:signin')
def vote_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.voter.add(request.user)
    return redirect('vapeasy:review_detail', review_id=review.id)

@login_required(login_url='common:signin')
def vote_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.voter.add(request.user)
    return redirect('vapeasy:review_detail', review_id=comment.review.id)