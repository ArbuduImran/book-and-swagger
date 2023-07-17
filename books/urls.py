from rest_framework import routers
from .views import *


# urlpatterns = [
#     path('random-quote/', RandomQuoteAPIView.as_view(), name='random-quote'),
# ]


router = routers.DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'random-quote', RandomQuoteAPIView, basename='random-quote')



urlpatterns = router.urls
