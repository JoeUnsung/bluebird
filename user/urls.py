from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),  # 회원 가입 URL 패턴입니다.
]
