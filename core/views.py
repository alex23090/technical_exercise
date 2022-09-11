from django.shortcuts import render
from .models import Profile, Game
# Create your views here.


def home(reqeust):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(reqeust, 'index.html', context)