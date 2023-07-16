from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from pydantic import generics
from rest_framework.viewsets import ModelViewSet
from .pagination import *
from .models import Book
# Create your views here.

from .serializer import BookSerializers


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializers
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = 'title author description'.split()
    pagination_class = StandardResultsSetPagination
