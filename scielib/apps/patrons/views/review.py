from rest_framework import filters, viewsets
from url_filter.integrations.drf import DjangoFilterBackend

from ..models.review import Review
from ..serializers.review import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.
    """

    queryset = Review.objects.all(
        ).select_related(
            'book',
            'patron',
        )

    serializer_class = ReviewSerializer

    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend,
    )
    filter_fields = (
        'id',
        'book',
        'patron',
        'review_score',
    )
    search_fields = (
        'review_text',
    )
