from django.contrib import admin
from .models import LottoTicket, LottoDraw

@admin.register(LottoTicket)
class LottoTicketAdmin(admin.ModelAdmin):
    list_display = ('numbers', 'is_auto', 'created_at')
    list_filter = ('is_auto',)

@admin.register(LottoDraw)
class LottoDrawAdmin(admin.ModelAdmin):
    list_display = ('draw_number', 'winning_numbers', 'created_at')
