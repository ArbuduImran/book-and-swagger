from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)

urlpatterns = router.urls
