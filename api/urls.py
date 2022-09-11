from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('games/', views.get_games, name='games'),
    path('user-info/', views.UserActions.as_view(), name='user-info'),
    path('add-game/', views.UserActions.as_view(), name='add-game'),
]