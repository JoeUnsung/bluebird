from django.shortcuts import render, get_object_or_404
from .models import CaseList

def case_list(request):
    '''
    사건 리스트 보여주는 함수뷰
    :param request:
    :return:
    '''
    # CaseList 모델의 모든 데이터를 가져옴
    case_list = CaseList.objects.all()

    # context에 case_list 추가하여 HTML에 전달
    context = {'case_list': case_list}
    return render(request, 'case_list/list.html', context)


def case_detail(request, pk=None):
    '''
    pk 기반으로
    :param request:
    :param pk:
    :return:
    '''
    if pk is None:
        pk = 1

    case = get_object_or_404(CaseList, pk=pk)
    return render(request, 'case_detail.html', {'case': case})

