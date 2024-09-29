from django.contrib import admin
from player.models import Player


# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Player, PlayerAdmin)
