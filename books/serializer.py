from .models import Book
from rest_framework.serializers import ModelSerializer


class BookSerializers(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
