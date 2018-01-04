from django.conf.urls import include, url
from .views import SpotifyBotView

app_name = 'spotify'
urlpatterns = [
    url('^spotify/?$', SpotifyBotView.as_view(), name='spotify')
]
