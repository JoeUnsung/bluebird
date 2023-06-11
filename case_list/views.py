from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import CaseList

def case_list(request):
    '''
    사건 리스트 보여주는 함수뷰
    :param request:
    :return:
    '''
    # CaseList 모델의 모든 데이터를 가져옴
    case_list = CaseList.objects.all() ## get_list_or_404로 이후에 각 지역별/권역별로 나눈 뒤에 적용

    # context에 case_list 추가하여 HTML에 전달
    context = {'case_list': case_list}
    return render(request, 'case_list/list.html', context)


def case_detail(request, pk=None):
    '''
    pk 기반으로 상세페이지에 필요한 정보를 렌더링하는 함수뷰
    :param request:
    :param pk:
    :return:
    '''
    if pk is None:
        # pk = 1
        case_num = '2021타경1767'
        # case_num = '2021타경17672222'

    # case = get_object_or_404(CaseList, pk=pk)
    case = get_object_or_404(CaseList, case_num=case_num)
    return render(request, 'case_list/detail.html', {'case': case})

