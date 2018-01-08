from django.views import generic
from django.http.response import HttpResponse
from django.conf import settings


class SpotifyBotView(generic.View):

    def get(self, request, *args, **kwargs):
        if self.request.GET.get(u'hub.verify_token') == settings.TOKEN_VERIFY:
            return HttpResponse(self.request.GET['hub.challenge'])

        if self.request.GET.get(u'hub.verify_token') is None:
            return HttpResponse('Error, token not found')

        return HttpResponse('Error, invalid token')
