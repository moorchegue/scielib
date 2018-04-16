from rest_framework import filters, viewsets
from url_filter.integrations.drf import DjangoFilterBackend

from ..models.book_collection import BookCollection
from ..serializers.book_collection import BookCollectionSerializer


class BookCollectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows book collections to be viewed or edited.
    """

    queryset = BookCollection.objects.all()

    serializer_class = BookCollectionSerializer

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )
    filter_fields = (
        'id',
    )
    search_fields = (
        'name',
    )
