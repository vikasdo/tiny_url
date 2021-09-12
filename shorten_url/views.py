from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView

from shorten_url.models import ShortUrlModel
from shorten_url.serializers import ShortUrlSerializer


class ShortenUrl(APIView):
    """Shorten a URL."""

    def post(self, request):
        data = {
            'url': request.data.get('url'),
            'short_id': ShortUrlModel.generate_short_id(),
        }

        serializer = ShortUrlSerializer(data=data)

        # if raised exception, it automatically
        # returns a 400 response with errors
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, 201)


class GetOriginalUrl(APIView):
    """Decode a URL short id into a the Original URL."""

    def get(self, request, short_id: str):
        try:
            obj = ShortUrlModel.objects.get(short_id=short_id)
            obj.increase_short_id_counter()
        except ObjectDoesNotExist:
            return Response({'error': 'Short url id does not exist.'}, 400)

        serializer = ShortUrlSerializer(obj)
        return Response(serializer.data, 200)
