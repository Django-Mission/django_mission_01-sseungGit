import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def lotto(request):
    
    #1. 변수 설정
    lotto_num = []

    #2. 랜덤 돌리기
    #for i in range(7):
    #    lotto_num.append(random.randint(1,46))
    lotto_num = random.sample(range(1,46),6)

    #3. 응답
    return render(request, 'lotto.html', {'lotto_num' : lotto_num})