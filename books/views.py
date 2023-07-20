from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .pagination import *
from .models import *
from random import choice
from .serializers import QuoteSerializers, BookSerializers
from rest_framework.response import Response


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = 'title author description'.split()
    pagination_class = StandardResultsSetPagination


class RandomQuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializers

    def list(self, request):
        quote = choice(self.queryset)
        serializer = QuoteSerializers(quote)
        return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SynonymSerializer, AntonymSerializer
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')


class SynonymView(APIView):
    serializer_class = SynonymSerializer

    def post(self, request):
        word = request.data.get('word', '')
        synonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
                if len(synonyms) >= 4:
                    break
            if len(synonyms) >= 4:
                break
        serializer = SynonymSerializer(data={'word': word, 'synonyms': synonyms[:4]})
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)



class AntonymView(APIView):
    serializer_class = AntonymSerializer

    def post(self, request):
        word = request.data.get('word', '')
        antonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if lemma.antonyms():
                    antonyms.append(lemma.antonyms()[0].name())
                    if len(antonyms) >= 4:
                        break
            if len(antonyms) >= 4:
                break
        serializer = AntonymSerializer(data={'word': word, 'antonyms': antonyms[:4]})
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


import requests
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Photo
from .serializers import PhotoSerializer


class PhotoSearchView(APIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, keyword):
        api_key = 'V93q2Wkj7o2bbPNEabw3b0Y3esdVV31pJMpQYbBo4hU  '
        url = 'https://api.unsplash.com/photos/random'

        headers = {
            'Authorization': f'Client-ID {api_key}'
        }

        params = {
            'query': keyword
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        photo_data = {
            'keyword': keyword,
            'image_url': data['urls']['regular']
        }

        serializer = self.serializer_class(data=photo_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
