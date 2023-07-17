from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class BookSerializers(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class QuoteSerializers(ModelSerializer):
    class Meta:
        model = Quote
        fields = ["text"]
