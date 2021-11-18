from django.contrib import admin
from .models import Jogos

class JogosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_jogo', 'data_lancamento', )
    list_display_links = ('nome_jogo', )

admin.site.register(Jogos, JogosAdmin)
