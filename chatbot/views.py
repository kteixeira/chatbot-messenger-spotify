import json
from pprint import pprint
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from .utils import post_facebook_message


class SpotifyBotView(generic.View):

    def get(self, request, *args, **kwargs):
        if self.request.GET.get(u'hub.verify_token') == settings.TOKEN_VERIFY:
            return HttpResponse(self.request.GET['hub.challenge'])

        if self.request.GET.get(u'hub.verify_token') is None:
            return HttpResponse('Error, token not found')

        return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))

        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    pprint(message)
                    post_facebook_message(message['sender']['id'],
                                          message['message']['text'])
        return HttpResponse()
