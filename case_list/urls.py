from django.urls import path
from .views import CaseListView, CaseDetailView

app_name = 'case_list'

urlpatterns = [
    path('', CaseListView.as_view(), name='case_list'),
    path('/detail/<int:pk>/', CaseDetailView.as_view(), name='case_detail'),
]

# from django.urls import path
# from . import views
#
# app_name = 'case_list'
#
# urlpatterns = [
#     path('', views.case_list, name='case_list')
#     , path('detail/<int:pk>/', views.case_detail, name='case_detail')  ## <int:pk> --> pk라는 변수를 int로 생성하고 case_list/detail/(?P<pk>[0-9]+)/\\Z 패턴으로 데이터를 받는다는 뜻
#     # , path('detail/1/', views.case_detail, name='case_detail')
#
# ]
