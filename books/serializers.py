from googletrans import Translator

from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class BookSerializers(ModelSerializer):
    translation = serializers.SerializerMethodField()

    def get_translation(self, obj):
        translator = Translator()
        translation = translator.translate(obj.title, dest='ru')
        return translation.text

    class Meta:
        model = Book
        fields = ('title', 'translation')


class QuoteSerializers(ModelSerializer):
    class Meta:
        model = Quote
        fields = ["text"]


from rest_framework import serializers


class SynonymSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=100)
    synonyms = serializers.ListField(child=serializers.CharField(max_length=100), required=False)


class AntonymSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=100)
    antonyms = serializers.ListField(child=serializers.CharField(max_length=100), required=False)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['keyword', 'image_url', 'created_at']