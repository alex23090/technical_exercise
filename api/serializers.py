from rest_framework import serializers
from core.models import Profile, Game


class ExtraProfile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'age', 'email']


class ExtraGame(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name']


class ProfileSerializer(serializers.ModelSerializer):
    games = ExtraGame(many=True)

    class Meta:
        model = Profile
        fields = ['id', 'name', 'age', 'email', 'games']


class GameSerializer(serializers.ModelSerializer):
    profile_set = ExtraProfile(many=True)

    class Meta:
        model = Game
        fields = ['name', 'profile_set']
