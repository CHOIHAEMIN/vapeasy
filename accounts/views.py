from django.shortcuts import render, redirect

# Create your views here.
def oauth(request):
    code = request.GET['code']
    print('code : ' + str(code))
    return redirect('vapeasy:index')

def kakao_login(requset):
    login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'
    client_id = '40bff2c99c09ea0b2fd8c2feb22e7c4b'
    # 운영단이면 도메인주소(포트번호80이면 8000도 생략)
    redirect_uri = 'http://127.0.0.1/oauth'

    login_request_uri += 'client_id=' + client_id
    login_request_uri += '&redirect_uri=' + redirect_uri
    login_request_uri += '&response_type=code'

    return redirect(login_request_uri)