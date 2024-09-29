from django.views.generic.base import TemplateView

from player.models import Player


class PlayerListView(TemplateView):
    template_name = 'player/player-list.html'
    model = Player

    # usar o repositório também nessa view

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['players'] = self.model.objects.all()
        return context
