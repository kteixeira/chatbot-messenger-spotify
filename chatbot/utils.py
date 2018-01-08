import json
import requests
from django.conf import settings
from pprint import pprint


def post_facebook_message(fbid, received_message):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(settings.ACCESS_TOKEN)

    response_msg = json.dumps({"recipient": {"id": fbid},
                               "message": {"text": received_message}})

    status = requests.post(post_message_url,
                           headers={"Content-Type": "application/json"},
                           data=response_msg)

    pprint(status.json())
