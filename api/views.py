from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from core.models import Profile, Game
from .serializers import ProfileSerializer, GameSerializer
from django.views.generic import View


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/games'},
        {'GET, POST': '/api/user-info'},
    ]

    return Response(routes)


# Get list of all games and users who connected to this games
@api_view(['GET'])
def get_games(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response({'games': serializer.data})


# Get info about current user and info about all connected games
@permission_classes([IsAuthenticated])
class UserActions(APIView):

    def get(self, request, *args, **kwargs):
        user = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(user, many=False)
        return Response({'current_user': serializer.data})

    def post(self, request, *args, **kwargs):
        game_data = request.data
        profile = Profile.objects.get(id=request.user.id)
        new_game = Game.objects.create(name=game_data['name'])
        profile.games.add(new_game)
        user = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(user, many=False)
        return Response(serializer.data)
