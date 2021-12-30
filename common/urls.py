from django.urls import path
from django.contrib.auth import views as auth_views



app_name = 'common'

urlpatterns = [
    path('signin/', auth_views.LoginView.as_view(template_name='common/signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(), name='signout'),

]