from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from game.models import Game
from home.views import get_complete_name

# Create your views here.

class GameListView(ListView):
    model = Game
    template_name = "game/game_list.html"
    context_object_name = "game_list"


class CreateUpdateView(CreateView):
    model = Game
    fields = '__all__'
    template_name = "game/game_form.html"
    success_url = '/game/list/'