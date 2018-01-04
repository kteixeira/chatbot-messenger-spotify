from django.views import generic
from django.http.response import HttpResponse


class SpotifyBotView(generic.View):

    def get(request, *args, **kwargs):
        return HttpResponse("It's Rock!")
