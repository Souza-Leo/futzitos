from django.urls import path, include # type: ignore

from player.views import PlayerListView, PlayerDetailView

urlpatterns = [
    path("", PlayerListView.as_view(), name="list"),
    path("jogador/<slug:player_id>/", PlayerDetailView.as_view(), name="detail"),
]
