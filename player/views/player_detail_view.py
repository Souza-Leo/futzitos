from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

from player.repositories.player_repository import PlayerRepository

# Alta coesão e Baixo acoplamento

# Cada classe deve estar em um arquivo
# A view não deve processar nada

# IDEAL = ALTA COESÃO (O MINIMO DE RESPONSABILIDADES POR CLASSES)

"""
COESÃO = RESPONSABILIDADE DE UM MÓDULO

MÓDULO = Class (Arquivo)

PlayerDetailView:

1 - Buscando jogador (processamento)
2 - Verificando se ele existe (processamento)
3 - Retornando a resposta da mesma
"""


class PlayerDetailView(TemplateView):
    template_name = 'player/player-detail.html'
    repository = PlayerRepository()

    def get(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        player = self.repository.get_by_id(kwargs["player_id"])

        if player:
            context["player"] = player
            return self.render_to_response(context)

        return HttpResponseRedirect(reverse('player:list'))
