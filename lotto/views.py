from django.shortcuts import render, redirect
from .models import LottoTicket
import random

def index(request):
    if request.method == 'POST':
        buy_type = request.POST.get('buy_type')
        if buy_type == 'manual':
            # 수동 번호 수집
            nums = [request.POST.get(f'n{i}') for i in range(1, 7)]
            num_str = ", ".join(sorted(nums, key=int))
            LottoTicket.objects.create(numbers=num_str, is_auto=False)
        else:
            # 자동 번호 생성
            auto_nums = random.sample(range(1, 46), 6)
            num_str = ", ".join(map(str, sorted(auto_nums)))
            LottoTicket.objects.create(numbers=num_str, is_auto=True)
        return redirect('/')
    
    return render(request, 'lotto/index.html')
