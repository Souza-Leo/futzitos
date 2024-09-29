from player.models import Player


class PlayerRepository:
    model = Player
    
    def get_by_id(self, id):
        try:
            return self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            return None
