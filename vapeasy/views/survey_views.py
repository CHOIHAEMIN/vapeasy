from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from ..models import Survey
from ..forms import SurveyForm, AnswerForm

@login_required(login_url='common:signin')
def survey(request):
    survey_list = Survey.objects.order_by('id')
    context = {'survey_list': survey_list}
    return render(request, "vapeasy/survey_list.html", context)

@login_required(login_url='common:signin')
def survey_answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        choice_list = request.POST.getlist('choice')
        if form.is_valid():
            answer = form.save(commit=False)
            answer.choice = choice_list
            answer.user = request.user
            answer.save()
            return redirect('vapeasy:index')
    else:
        survey_list = Survey.objects.order_by('id')
    return render(request, 'vapeasy/survey_list.html', {'survey_list': survey_list})


