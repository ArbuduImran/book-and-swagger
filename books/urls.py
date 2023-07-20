from django.urls import path , include

from rest_framework import routers
from .views import RandomQuoteViewSet, BookViewSet, AntonymView, SynonymView, PhotoSearchView

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'random-quote', RandomQuoteViewSet)



urlpatterns = [
    *router.urls,
    path('antonyms/', AntonymView.as_view(), name='antonyms'),
    path('synonyms/', SynonymView.as_view(), name='synonyms'),
    path('search/<str:keyword>/', PhotoSearchView.as_view()),
    path('', include(router.urls)),
]

