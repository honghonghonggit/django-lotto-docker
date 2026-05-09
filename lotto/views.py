from django.shortcuts import render, redirect
from .models import LottoTicket, LottoDraw
import random

def index(request):
    if request.method == 'POST':
        buy_type = request.POST.get('buy_type')
        if buy_type == 'manual':
            nums = [request.POST.get(f'n{i}') for i in range(1, 7)]
            num_str = ", ".join(sorted(nums, key=int))
            LottoTicket.objects.create(numbers=num_str, is_auto=False)
        else:
            auto_nums = random.sample(range(1, 46), 6)
            num_str = ", ".join(map(str, sorted(auto_nums)))
            LottoTicket.objects.create(numbers=num_str, is_auto=True)
        return redirect('/')
    
    # 내 티켓들과 최신 당첨 번호 가져오기
    my_tickets = LottoTicket.objects.all().order_by('-created_at')
    last_draw = LottoDraw.objects.all().order_by('-draw_number').first()
    
    # 당첨 비교 로직
    results = []
    for ticket in my_tickets:
        is_winner = "확인 전"
        if last_draw:
            if ticket.numbers == last_draw.winning_numbers:
                is_winner = "★ 1등 당첨! ★"
            else:
                is_winner = "낙첨"
        results.append({'ticket': ticket, 'is_winner': is_winner})

    return render(request, 'lotto/index.html', {'results': results, 'last_draw': last_draw})
