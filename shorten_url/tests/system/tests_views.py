from django.conf import settings
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class ShortenUrlViewTests(APITestCase):
    def setUp(self):
        self.shorten_url = reverse('shorten_url')
        self.data = dict(
            url='https://github.com/Fantaso/todo-app-django-rest-api',
        )

    def test_shorten_url(self):
        response = self.client.post(
            self.shorten_url,
            data=self.data,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn(settings.SITE_URL, response.data['short_id'])

    def test_shorten_url_data_invalidation(self):
        invalid_data = {'url': 'Not a valid url'}
        response = self.client.post(
            self.shorten_url,
            data=invalid_data,
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Enter a valid URL.', response.data['url'])

    def test_get_original_url(self):
        response = self.client.post(
            self.shorten_url,
            data=self.data,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn(settings.SITE_URL, response.data['short_id'])
        self.assertEqual(response.data['count'], 0)

        short_id = response.data['short_id'].replace(settings.SITE_URL, '')
        url_get = f'http://localhost:8000/{short_id}'
        response_get = self.client.get(url_get)

        self.assertEqual(response_get.data['count'], 1)
        self.assertEqual(response_get.data['url'], self.data['url'])
