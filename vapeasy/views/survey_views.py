from ast import And
from secrets import choice
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.contrib import messages
from vapeasy.views.product_views import product_list
from ..models import Survey, Product, Answer
from ..forms import SurveyForm, AnswerForm
import json

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
            
            #유저의 중복 응답을 막기위한 update
            overlap_answer = Answer.objects.filter(user_id = request.user.id)
            if overlap_answer:
                overlap_answer.update(choice = json.dumps(choice_list))
            else:
                # 템플릿단의 체크박스 밸류를 json을 통해 리스트로 저장함
                answer.choice = json.dumps(choice_list)
                answer.user = request.user
                answer.save()
            return redirect('vapeasy:survey_result')
    else:
        survey_list = Survey.objects.order_by('id')
    return render(request, 'vapeasy/survey_list.html', {'survey_list': survey_list})

@login_required(login_url='common:signin')
def survey_result(request):
    # answer = get_object_or_404(Answer, user_id=user_id)
    # if request.user != answer.user:
    #     messages.error(request, '다른 회원의 추천 리스트입니다.')
    #     return redirect('vapeasy:index')
    # else:
    # 요청 유저 id와 선택데이터 유저 id를 대조하여 고른 후
    # choice 컬럼의 쿼리셋을 가져옴
    answer_set = Answer.objects.filter(user_id = request.user.id).values('choice')
    
    # 키밸류형태의 쿼리셋을 밸류만 잘라 json으로 밸류를 리스트로 가져옴
    # ex) answers = answer[0]['choice'] <======= DB에서 str로 저장&읽음, 원하는 쿼리셋활용이 안된다.
    answer_json = json.loads(answer_set[0]['choice'])
    
    recommend_products = Product.objects.filter(
        Q(category__in = answer_json) &
        Q(menthol__in = answer_json) &
        Q(sweet__in = answer_json)
        )
    # print(recommend_products)
    context = {'recommend_products': recommend_products }
    return render(request, 'vapeasy/survey_result.html', context)


