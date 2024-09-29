from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

from player.repositories.player_repository import PlayerRepository


class PlayerDetailView(TemplateView):
    """
        A view não deve processar nada,
        apenas chamar quem faz o processamento (repository, use_case, service)
    """

    template_name = 'player/player-detail.html'
    repository = PlayerRepository()

    def get(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        player = self.repository.get_by_id(kwargs["player_id"])

        if player:
            context["player"] = player
            return self.render_to_response(context)

        return HttpResponseRedirect(reverse('player:list'))
