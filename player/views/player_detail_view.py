from django.views.generic.base import TemplateView

from django.http import HttpResponseRedirect
from django.urls import reverse

from player.models import Player

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
    model = Player

    def get(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if not context['player']:
            return HttpResponseRedirect(reverse('player:list'))

        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        try:
            context['player'] = self.model.objects.get(id=kwargs['player_id'])
        except self.model.DoesNotExist:
            context['player'] = None

        return context
