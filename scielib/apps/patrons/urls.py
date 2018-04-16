from django.conf.urls import url, include
from rest_framework import routers

from .views import (
    patron,
    borrowing,
    review,
)


router = routers.DefaultRouter()
router.register(r'patrons', patron.PatronViewSet)
router.register(r'borrowings', borrowing.BorrowingViewSet)
router.register(r'reviews', review.ReviewViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
]
