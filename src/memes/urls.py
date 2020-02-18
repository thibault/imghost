from django.urls import path

from memes import views


urlpatterns = [
    path('<slug:unique_key>/', views.meme, name='meme'),
]
