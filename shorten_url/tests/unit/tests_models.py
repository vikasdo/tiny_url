from django.test import TestCase

from shorten_url.models import ShortUrlModel


class ShortUrlModelUnitTests(TestCase):
    def setUp(self):
        self.data = dict(
            url='https://github.com/Fantaso/todo-app-django-rest-api',
            short_id='Shy7s3',
        )

    def test_create_url(self):
        url_obj = ShortUrlModel(**self.data)

        self.assertEqual(url_obj.url, self.data['url'])
        self.assertEqual(url_obj.short_id, self.data['short_id'])
        self.assertEqual(url_obj.count, 0)
