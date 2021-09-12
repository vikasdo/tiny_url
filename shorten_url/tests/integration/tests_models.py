from django.test import TestCase

from shorten_url.models import ShortUrlModel


class ShortUrlModelIntegrationTests(TestCase):
    def setUp(self):
        self.data = dict(
            url='https://github.com/Fantaso/todo-app-django-rest-api',
            short_id='Shy7s3',
        )
        self.url_obj = ShortUrlModel.objects.create(**self.data)

    def test_increase_url_counter(self):
        url_obj = ShortUrlModel.objects.get(short_id=self.data['short_id'])

        self.assertEqual(url_obj.count, 0)
        url_obj.increase_short_id_counter()
        self.assertEqual(url_obj.count, 1)

    def test_generate_short_id(self):
        short_id = ShortUrlModel.generate_short_id()

        self.assertEqual(len(short_id), ShortUrlModel.ID_LENGTH)
