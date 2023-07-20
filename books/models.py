from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField()


class Quote(models.Model):
    text = models.TextField()


class Photo(models.Model):
    keyword = models.CharField(max_length=100)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
