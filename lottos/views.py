import random
import re
from django.shortcuts import render

# Create your views here.

def lotto(request):

    return render(request,'lotto.html')

def result(request):
    
    # 입력값 받기
    lotto_num = request.GET.get('lotto_num')
    result_list = []
    
    # 입력값만큼 로또 돌리기
    for i in range(int(lotto_num)):
        result_list.insert(i, random.sample(range(1,46),6))

    print(result_list)

    return render(request, 'result.html', 
        {'lotto_num' : lotto_num, 'result_dict' : result_list})
