from django.urls import path, include

from player.views import PlayerListView

urlpatterns = [
    path("list/", PlayerListView.as_view(), name="list"),
    # path("detail/", PlayerDetailView.as_view(), name="detail"),
]

""""
    - urls
        /player = rota
        - player (include)
            - urls

    futdb.com/player/list
"""
