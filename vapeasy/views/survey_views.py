from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from ..models import Review, Comment, Survey
from ..forms import ReviewForm

def survey(request):
    survey = Survey.objects.get(id=1)
    context = {'survey': survey}
    return render(request, "vapeasy/survey_list.html", context)