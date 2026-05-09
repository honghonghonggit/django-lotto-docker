from django.db import models
import random

class LottoTicket(models.Model):
    numbers = models.CharField(max_length=100)  # 예: "1, 5, 12, 23, 34, 45"
    created_at = models.DateTimeField(auto_now_add=True)
    is_auto = models.BooleanField(default=False)

    def __str__(self):
        return f"{'자동' if self.is_auto else '수동'} - {self.numbers}"

class LottoDraw(models.Model):
    draw_number = models.IntegerField(unique=True) # 회차
    winning_numbers = models.CharField(max_length=100) # 당첨번호
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.draw_number}회차 당첨번호: {self.winning_numbers}"
