from django.contrib import admin
from django.urls import path, include

from player import urls as player_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("player/", include(("player.urls", "player"), namespace="player")),
]
