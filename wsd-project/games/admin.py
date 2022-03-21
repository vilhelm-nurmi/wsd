from django.contrib import admin
from .models import Game,Highscore,SavedGame,Transaction

admin.site.register(Game)
admin.site.register(Highscore)
admin.site.register(SavedGame)
class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ('time_stamp',)
admin.site.register(Transaction,TransactionAdmin)
