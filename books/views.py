from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Book
# Create your views here.

from .serializer import BookSerializers


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializers
    queryset = Book.objects.all()
