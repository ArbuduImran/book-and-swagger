from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .pagination import *
from .models import *
from random import choice
from rest_framework.response import Response
from .serializer import QuoteSerializers,BookSerializers


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializers
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = 'title author description'.split()
    pagination_class = StandardResultsSetPagination





class RandomQuoteAPIView(ModelViewSet):
    queryset = Quote.objects.all()
    quote = choice(Quote.objects.all())
    serializer_class = QuoteSerializers(quote)


