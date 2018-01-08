from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings


class TestSpotifyBotView(TestCase):

    def setUp(self):
        self.url = reverse('chatbot:spotify')
        self.client = Client()
        self.challenge = 'Test Challenge'
        self.token = settings.TOKEN_VERIFY

    def test_get_token_not_found(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Error, token not found')

    def test_get_invalid_token(self):
        response = self.client.get(
            self.url, {
                'hub.verify_token': '123456798',
                'hub.challenge': self.challenge})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Error, invalid token')

    def test_get_valid_token(self):
        response = self.client.get(
            self.url, {
                'hub.verify_token': self.token,
                'hub.challenge': self.challenge})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, bytes(self.challenge,
                                                 encoding='utf-8'))
