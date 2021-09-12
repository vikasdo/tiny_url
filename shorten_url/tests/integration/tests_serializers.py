from django.test import TestCase

from shorten_url.models import ShortUrlModel
from shorten_url.serializers import ShortUrlSerializer


class ShortUrlSerializerIntegrationTests(TestCase):
    def setUp(self):
        self.data = dict(
            url='https://github.com/Fantaso/todo-app-django-rest-api',
            short_id='Shy7s3',
        )

    def test_url_serializer_create_url_model(self):
        url_obj = ShortUrlModel.objects.filter(short_id=self.data['short_id']).first()

        self.assertIsNone(url_obj)

        url_serializer = ShortUrlSerializer(data=self.data)
        url_serializer.is_valid()
        url_serializer.save()

        url_obj = ShortUrlModel.objects.get(short_id=self.data['short_id'])

        self.assertEqual(url_obj.short_id, self.data['short_id'])
