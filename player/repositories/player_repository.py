from player.models import Player


class PlayerRepository:
    model = Player

    def get_by_id(self, id):
        try:
            return self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            return None

    def get_all(self):
        # tarefitas
        pass

    def get_by_params(self, params):
        pass
