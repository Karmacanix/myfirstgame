
from django.urls import path
from .views import GameListView, CreateUpdateView

urlpatterns = [
    path("list/", GameListView.as_view(), name='game_list'),    
    path("create/", CreateUpdateView.as_view(), name='create_game'),
    # path("update/<int:pk>/", CampaignUpdateView.as_view(), name='campaign_update'),
]
